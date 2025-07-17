from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Event, RSVP
from app.classifier.predict_event import predict_event_category

main = Blueprint('main', __name__)

@main.route('/')
def index():
    query = request.args.get('query', '').lower()
    events = Event.query.all()
    if query:
        events = [e for e in events if query in e.EventName.lower() or query in e.Description.lower()]
    return render_template('index.html', events=events, query=query)

@main.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['EventName']
        date = request.form['Date']
        location = request.form['Location']
        desc = request.form['Description']
        event_type = predict_event_category(name, location, desc)

        new_event = Event(EventName=name, Date=date, Location=location, Description=desc, Type=event_type)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_event.html')

@main.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        event.EventName = request.form['EventName']
        event.Date = request.form['Date']
        event.Location = request.form['Location']
        event.Description = request.form['Description']
        event.Type = predict_event_category(event.EventName, event.Location, event.Description)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit_event.html', event=event,event_id=event_id)

@main.route('/delete/<int:event_id>')
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/rsvp/<int:event_id>', methods=['GET', 'POST'])
def rsvp(event_id):
    event = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        name = request.form['name']
        guests = int(request.form['guests'])
        new_rsvp = RSVP(name=name, guests=guests, event=event)
        db.session.add(new_rsvp)
        db.session.commit()
        return redirect(url_for('main.rsvp', event_id=event_id))

    rsvps = RSVP.query.filter_by(event_id=event_id).all()
    total_attendance = sum(r.guests for r in rsvps)

    return render_template('rsvp.html', event=event, rsvps=rsvps,event_id=event_id, total_attendance=total_attendance)

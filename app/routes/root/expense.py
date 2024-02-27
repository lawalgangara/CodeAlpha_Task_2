from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.models.user import Expense


@app.route('/register', methods=['GET', 'POST'])
def expense_page():
    if request.method == 'POST':

        # Get the form data
        form_data = request.form

        # Create an expense object and add it to the database
        expense = Expense(
            title=form_data['expense_title'],
            amount=form_data['expense_amount'],
            date=form_data['expense_date']
        )

        db.session.add(expense)
        db.session.commit()

        flash('You have successfully added an expense', 'success')

        # Redirect to the page to display user inputs
        return redirect(url_for('user_inputs'))

    return render_template('root/expense.html')

@app.route('/user_inputs')
def user_inputs():
    # Retrieve all user inputs from the database
    expenses = Expense.query.all()

    return render_template('root/user_inputs.html', expenses=expenses)

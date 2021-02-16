## Guiding Principles ##

1. Keep it simple - this is a small challenge so I didn't want any eccessive overhead (e.g. heavy libraries/frameworks like ReactJS or external services like Mysql/Postgres or Redis).
2. Resemble production code - create a basic structure that would allow the project to grow into a fullfledged online spreadsheet app.
3. Avoid future proofing but lay an extensible structure.


### UI ###

I chose to include [Milligram](https://milligram.io) as my CSS framework, more to showcase how it can be included rather than the style it provides.


### Frontend ###

After some indecision I finally chose to use [Svelte](https://svelte.dev). I felt the project would benefit from data binding, state management and other facilities, but still I didn't want a whole framework like ReactJS or VueJS.

Calculations are performed in this part of the application, given they are not particularly heavy on the CPU (although it's worth noticing that I'm using a recursive function for those cells that contain a reference to another formula).


### Code structure ###

For such a small example it wouldn't be by any means necessary but, imagining this as an MVP on which to build future functionalities, it would become soon necessary to split the code; for this purpose I used Flask's Blueprints.


### Persistence ###

In observance to my guiding principles I choose SQLite for persisting the values and, while I could've used flat files, it wouldn't be a realistic setup in most circumstances. At the same time I opted to use SQLAlchemy as my ORM since it's a very common setup.

The code for the only table present is in the *migrations* directory, where I could store and version any possible change to the db structure.

A nice feature the RDBMS gives in this implementation is the possibility of versioning the values, so I'd be able to create an undo functionality and, in a multiuser environment, it'd be enough to add a new users table to keep track of who edited what.

On start the server will connect to the DB and fetch the latest value (denoted by the timestamp) for all cells and, when undoing one's entries, the server could query the previous version for a specific cell.


### Communication ###

Given the possibility of constant updating I choose to use websockets to mantain an open connection and reduce once again overhead.

Furthermore, if we'd decide to expand the project to become a collaborative spreadsheet, this would allow to push other users' changes in realtime to each of them.


## Usage ##

### Setup ###
1. Set up your virtualenv: `python3 -m venv interview_venv`
2. Source the `activate` script: `source interview_venv/bin/activate`
3. Install the dependencies in your virtualenv: `pip install -r requirements.txt`
4. Create db: `flask db upgrade`
4. Install node modules dependencies: `yarn --cwd spreadsheet/client`

### Run ###

#### Dev mode ####
1. Build FE in watch mode: `yarn --cwd spreadsheet/client dev`
2. Run the server: `FLASK_ENV=development FLASK_APP=spreadsheet flask run -p 8000`

*Note this will use long polling instead of websocket*

#### Prod mode ####
1. Build FE: `yarn --cwd spreadsheet/client build`
2. Run the server: `gunicorn "spreadsheet:create_app()"`


Visit [http://localhost:8000](http://localhost:8000).


## Final considerations ##

While I could've done the challenge in my current language of choice (Elixir), I used the occasion to learn a bit about Flask and Svelte (neither of which I had used before).

Initially I thought this would be a very easy task, but the more I got to think how I could implement something vaguely resembling Google's spreadsheets I understood it would be way more complicated than estimated. The biggest difficulty turned out to be setting up the project, figuring out how to arrange Svelte inside Flask and install compatible versions of packages to support Socket.io.

On the technical side, I layed the foundation for a few out-of-scope improvements which wouldn't require excessive amount of time to add (but I didn't implement them not to "pollute" the code):

- Undo/Redo button
    HOW:
    Ask the backend all the records for the selected cell and navigate forth and back through the values using these buttons.

- Reset button
    HOW:
    On clicking the reset button instruct the backend to truncate the "cells" table and return an empty object.

- Button to Add/Remove Rows/Columns (4 in total)
    HOW:
    On clicking add/remove button for adding/removing rows/columns increase/decrease the value for rows/columns and update the store. This will rerender the Sheet component and its children.

    PROBLEMS:
    - Need to save or calculate the last row and column when reloading
    - when more than 26 columns need to concat letters e.g. column 27 is AA

- Add Navigation With Arrows
    HOW:
    On the keyup handler check the key code and increase/decrease accordingly the row or column; set the selected cell to the new position on move focus to that cell.
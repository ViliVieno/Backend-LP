This is an backend made for my backend course. In it, the user can make players and events for them with different routers. It was made using FastApi and Uvicorn.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
For the database, SQLite was used. 

To run the app, you need to use pip install -r requirements.txt and then run it with:
python -m uvicorn app.main:app --reload / uvicorn app.main:app <- If you are in the folder you pull this in
OR
python -m fastapi dev main.py / fastapi dev main.py <- If you are in the app folder

For reasons unspoken I had to use python -m for my own testings.

The program was made by me, with help from the work we did in class and in some sections by ChatGPT, which was mainly used to learn or make something better. Below, I have listed everything that I used AI for. For the sake of clarity, I made comments on the codes, where AI was used.

Working Prompts
--------------------------------------------------------------------------------------------------------------
Make players with POST /players/
Get all players with GET /players/
Get specific player with GET /players/{id}?player_id=?
Get players events with GET /players/?/events?type=?, there are only two valid types: level_started and level_solved
Make events for players with POST /players/?/events

Get all events with GET /events/
Get all events of a specific type GET /events/type/level_solved or /events/type/level_started

AI Part.
--------------------------------------------------------------------------------------------------------------
The uses of package typing and the imports List and Optional were made with the use and recommendation of AI in: players.py, player_events.py, event_crud.py, player_crud.py.
I commented these parts to explain them better, as these were fairly simple to use.

AI on player_crud.py: The get_player_with_events was made with a lot of help from chatgpt.

AI Was also widely used to start some of them, before being replaced with new code.


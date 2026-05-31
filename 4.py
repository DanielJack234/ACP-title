from graphviz import Digraph

# Create flowchart
dot = Digraph(comment="Daily Routine", format="png")
dot.attr(rankdir="TB", size="8,12")

# Nodes
dot.node("start", "Start of Day", shape="ellipse", style="filled", fillcolor="lightgreen")
dot.node("wake", "Wake Up", shape="box", style="filled", fillcolor="lightyellow")
dot.node("morning", "Morning Routine\n(Prayer, Hygiene, etc.)", shape="box", style="filled", fillcolor="lightblue")
dot.node("exercise", "Exercise / Workout", shape="box")
dot.node("breakfast", "Breakfast", shape="box")
dot.node("work", "Work / Study", shape="box", style="filled", fillcolor="lightpurple")
dot.node("lunch", "Lunch Break", shape="box")
dot.node("afternoon", "Afternoon Tasks", shape="box")
dot.node("dinner", "Dinner", shape="box")
dot.node("evening", "Evening Wind Down\n(Reading, Family, Relax)", shape="box")
dot.node("sleep", "Sleep", shape="ellipse", style="filled", fillcolor="lightpink")

# Edges
dot.edge("start", "wake")
dot.edge("wake", "morning")
dot.edge("morning", "exercise", label="30-60 min")
dot.edge("morning", "breakfast", label="30-60 min")
dot.edge("exercise", "work")
dot.edge("breakfast", "work")
dot.edge("work", "lunch")
dot.edge("lunch", "afternoon")
dot.edge("afternoon", "dinner")
dot.edge("dinner", "evening")
dot.edge("evening", "sleep")

# Render and save
dot.render("daily_routine", view=True)
print("Flowchart saved as 'daily_routine.png'")
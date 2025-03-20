import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return {"error": "Template must be a string."}
    if not template:
        return {"error": "Template is empty, no output files generated."}
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        return {"error": "attendees must be a list of dictionaries"}
    if not attendees:
        return {"error": "No data provided, no output files generated"}

    for i, item in enumerate(attendees, start=1):
        name = item.get("name")
        title = item.get("event_title")
        date = item.get("event_date")
        location = item.get("event_location")

        if name is None:
            name = "N/A"
        if title is None:
            title = "N/A"
        if date is None:
            date = "N/A"
        if location is None:
            location = "N/A"

        personalized_template = template.replace("{name}", name)
        personalized_template = personalized_template.replace("{event_title}", title)
        personalized_template = personalized_template.replace("{event_date}", date)
        personalized_template = personalized_template.replace("{event_location}", location)

        file_name = f"output_{i}.txt"
        if os.path.exists(file_name):
             continue
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(personalized_template)

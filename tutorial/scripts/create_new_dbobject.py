from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
print(Question.objects.all())

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()

# Now it has an ID.
print(q.id)

# Access model field values via Python attributes.
print(q.question_text)

print(q.pub_date)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
print(Question.objects.all())
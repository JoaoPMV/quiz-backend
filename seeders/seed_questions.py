from app import app
from models.user import db
from models.question import Question
import json

questions_seed = [
{
    "question": "Choose the sentence that correctly uses the phrasal verb 'put up with':",
    "alternatives": [
      {"id": "a", "text": "I can no longer put up with his constant interruptions during meetings."},
      {"id": "b", "text": "I can no longer put with up his constant interruptions during meetings."},
      {"id": "c", "text": "I can no longer put over with his constant interruptions during meetings."},
      {"id": "d", "text": "I can no longer put down with his constant interruptions during meetings."},
      {"id": "e", "text": "I can no longer put through with his constant interruptions during meetings."}
    ],
    "correct_answer": "a",
    "level": "c1",
    "content": "phrasal verbs",
    "explanation": "The phrasal verb 'put up with' means to tolerate or endure something unpleasant. The correct structure is 'put up with + noun or gerund'."
  },

]

def norm(v):
    return (v or "").strip().lower()

def alt_sig(alts):
    return json.dumps(alts, sort_keys=True, ensure_ascii=False)

with app.app_context():
    created = 0
    skipped = 0

    for q in questions_seed:
        # DUPLICATA = tudo igual (incluindo alternativas)
        existing = Question.query.filter_by(
            question=q["question"],
            level=q["level"],
            content=q["content"],
            correct_answer=q["correct_answer"],
        ).all()

        duplicate = any(alt_sig(e.alternatives) == alt_sig(q["alternatives"]) for e in existing)

        if duplicate:
            skipped += 1
            continue

        db.session.add(Question(**q))
        created += 1

    db.session.commit()
    print(f"✅ Seed finalizado. Criadas: {created} | Ignoradas (duplicadas): {skipped}")
from app import app
from models.user import db
from models.question import Question
import json

questions_seed = [

  {
    "question": "Which sentence expresses a cautious claim rather than absolute certainty?",
    "alternatives": [
      { "id": "a", "text": "The evidence would seem to suggest that the policy was ineffective." },
      { "id": "b", "text": "The evidence proves that the policy was ineffective." },
      { "id": "c", "text": "The policy was definitely ineffective." },
      { "id": "d", "text": "There is no doubt that the policy was ineffective." },
      { "id": "e", "text": "The policy was unquestionably ineffective." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Would seem to suggest weakens the claim and presents it cautiously."
  },
  {
    "question": "Which expression is most appropriate for cautiously introducing a possible explanation?",
    "alternatives": [
      { "id": "a", "text": "One possible explanation is that the results were affected by external factors." },
      { "id": "b", "text": "The only explanation is that the results were affected by external factors." },
      { "id": "c", "text": "The results were certainly affected by external factors." },
      { "id": "d", "text": "There is absolutely no other explanation." },
      { "id": "e", "text": "The results unquestionably resulted from external factors." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "One possible explanation signals that the proposed explanation is not presented as certain."
  },
  {
    "question": "Which sentence shows strong academic caution?",
    "alternatives": [
      { "id": "a", "text": "These findings may indicate a broader change in consumer behavior." },
      { "id": "b", "text": "These findings definitely indicate a broader change in consumer behavior." },
      { "id": "c", "text": "These findings prove a broader change in consumer behavior." },
      { "id": "d", "text": "These findings unquestionably establish a broader change in consumer behavior." },
      { "id": "e", "text": "These findings cannot possibly mean anything else." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "May indicate presents the interpretation as possible rather than certain."
  },
  {
    "question": "Which sentence appropriately avoids making an absolute generalization?",
    "alternatives": [
      { "id": "a", "text": "This approach tends to be more effective in complex cases." },
      { "id": "b", "text": "This approach is always more effective in complex cases." },
      { "id": "c", "text": "This approach is unquestionably more effective in every case." },
      { "id": "d", "text": "This approach is never ineffective." },
      { "id": "e", "text": "This approach invariably produces better results." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Tends to limits the claim and avoids suggesting that the pattern applies universally."
  },
  {
    "question": "Which phrase is most suitable for expressing tentative agreement?",
    "alternatives": [
      { "id": "a", "text": "I would tend to agree with that interpretation." },
      { "id": "b", "text": "I completely agree without reservation." },
      { "id": "c", "text": "That interpretation is unquestionably correct." },
      { "id": "d", "text": "There is no possible objection to that interpretation." },
      { "id": "e", "text": "I absolutely endorse every aspect of that interpretation." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Would tend to agree expresses agreement while leaving room for qualification."
  },
  {
    "question": "Which sentence most clearly expresses uncertainty?",
    "alternatives": [
      { "id": "a", "text": "It is possible that the discrepancy reflects a methodological limitation." },
      { "id": "b", "text": "The discrepancy unquestionably reflects a methodological limitation." },
      { "id": "c", "text": "The discrepancy certainly reflects a methodological limitation." },
      { "id": "d", "text": "The discrepancy proves the methodological limitation." },
      { "id": "e", "text": "The discrepancy can only reflect a methodological limitation." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "It is possible that explicitly presents the explanation as uncertain."
  },
  {
    "question": "Which sentence uses a modal verb to hedge a conclusion?",
    "alternatives": [
      { "id": "a", "text": "The decline could be attributed to changes in consumer preferences." },
      { "id": "b", "text": "The decline must be attributed to changes in consumer preferences." },
      { "id": "c", "text": "The decline is definitely attributed to changes in consumer preferences." },
      { "id": "d", "text": "The decline proves the changes in consumer preferences." },
      { "id": "e", "text": "The decline is unquestionably caused by changes in consumer preferences." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could presents attribution as one possible interpretation rather than a certainty."
  },
  {
    "question": "Which sentence is appropriately cautious in an academic context?",
    "alternatives": [
      { "id": "a", "text": "The results appear to support the hypothesis, although further research is needed." },
      { "id": "b", "text": "The results conclusively prove the hypothesis." },
      { "id": "c", "text": "The hypothesis has been completely proven." },
      { "id": "d", "text": "The results leave absolutely no room for doubt." },
      { "id": "e", "text": "Further research is clearly unnecessary." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Appear to support and further research is needed both introduce appropriate caution."
  },
  {
    "question": "Which phrase weakens a claim without rejecting it completely?",
    "alternatives": [
      { "id": "a", "text": "To some extent" },
      { "id": "b", "text": "Under no circumstances" },
      { "id": "c", "text": "Without exception" },
      { "id": "d", "text": "Beyond any doubt" },
      { "id": "e", "text": "Invariably" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "To some extent limits the strength or scope of a statement."
  },
  {
    "question": "Which sentence expresses a strong personal stance?",
    "alternatives": [
      { "id": "a", "text": "I strongly maintain that the proposed reform is necessary." },
      { "id": "b", "text": "The reform might perhaps be necessary." },
      { "id": "c", "text": "The reform could potentially be necessary." },
      { "id": "d", "text": "It is conceivable that the reform is necessary." },
      { "id": "e", "text": "The reform may possibly be necessary." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Strongly maintain explicitly signals a firm position."
  },
  {
    "question": "Which sentence is the most appropriately hedged?",
    "alternatives": [
      { "id": "a", "text": "The policy could potentially have unintended consequences." },
      { "id": "b", "text": "The policy will definitely have unintended consequences." },
      { "id": "c", "text": "The policy certainly has unintended consequences." },
      { "id": "d", "text": "The policy inevitably has unintended consequences." },
      { "id": "e", "text": "The policy unquestionably has unintended consequences." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could potentially presents the consequences as a possibility."
  },
  {
    "question": "Which expression is most suitable for indicating that evidence is limited?",
    "alternatives": [
      { "id": "a", "text": "The available evidence is somewhat limited." },
      { "id": "b", "text": "The available evidence is absolutely conclusive." },
      { "id": "c", "text": "The available evidence is beyond dispute." },
      { "id": "d", "text": "The available evidence proves everything." },
      { "id": "e", "text": "The available evidence is unquestionably sufficient." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Somewhat limited qualifies the statement and signals that the evidence has restrictions."
  },
  {
    "question": "Which sentence uses an appropriate stance marker?",
    "alternatives": [
      { "id": "a", "text": "Arguably, the most significant issue is the lack of transparency." },
      { "id": "b", "text": "Obviously, the most significant issue is unquestionably the lack of transparency." },
      { "id": "c", "text": "The most significant issue is undeniably the lack of transparency." },
      { "id": "d", "text": "The lack of transparency is unquestionably the only issue." },
      { "id": "e", "text": "There can be no possible disagreement about the issue." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Arguably presents the statement as a defensible interpretation rather than an unquestionable fact."
  },
  {
    "question": "Which sentence appropriately acknowledges an alternative interpretation?",
    "alternatives": [
      { "id": "a", "text": "It could equally be argued that the decline resulted from broader economic pressures." },
      { "id": "b", "text": "There is only one possible interpretation of the decline." },
      { "id": "c", "text": "The decline can only have resulted from one specific factor." },
      { "id": "d", "text": "No alternative interpretation is remotely plausible." },
      { "id": "e", "text": "The original interpretation is unquestionably correct." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could equally be argued acknowledges another reasonable interpretation."
  },
  {
    "question": "Which sentence avoids overstating the significance of the findings?",
    "alternatives": [
      { "id": "a", "text": "The findings may have broader implications for future research." },
      { "id": "b", "text": "The findings will unquestionably transform future research." },
      { "id": "c", "text": "The findings are guaranteed to revolutionize the field." },
      { "id": "d", "text": "The findings will certainly change everything." },
      { "id": "e", "text": "The findings inevitably determine the future of the field." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "May have broader implications indicates a possible significance without exaggeration."
  },
  {
    "question": "Which expression is most appropriate when the writer wants to distance themselves slightly from a claim?",
    "alternatives": [
      { "id": "a", "text": "It would appear that the current approach is insufficient." },
      { "id": "b", "text": "It is absolutely certain that the current approach is insufficient." },
      { "id": "c", "text": "The current approach is unquestionably insufficient." },
      { "id": "d", "text": "There is no doubt that the current approach is insufficient." },
      { "id": "e", "text": "The current approach is undoubtedly insufficient." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Would appear to distance the writer from making a fully categorical claim."
  },
  {
    "question": "Which sentence expresses a qualified criticism?",
    "alternatives": [
      { "id": "a", "text": "The proposal is, to some extent, overly ambitious." },
      { "id": "b", "text": "The proposal is completely unrealistic in every respect." },
      { "id": "c", "text": "The proposal is unquestionably disastrous." },
      { "id": "d", "text": "The proposal is entirely unacceptable." },
      { "id": "e", "text": "The proposal is beyond any possible criticism." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "To some extent limits the criticism rather than presenting it as absolute."
  },
  {
    "question": "Which sentence most clearly expresses a tentative conclusion?",
    "alternatives": [
      { "id": "a", "text": "Taken together, the findings would seem to indicate a gradual shift in attitudes." },
      { "id": "b", "text": "Taken together, the findings definitively establish a complete change in attitudes." },
      { "id": "c", "text": "The findings prove that attitudes have completely changed." },
      { "id": "d", "text": "The findings unquestionably establish the final explanation." },
      { "id": "e", "text": "The findings leave no possibility of another conclusion." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Would seem to indicate presents the conclusion cautiously."
  },
  {
    "question": "Which sentence uses a cautious reporting verb?",
    "alternatives": [
      { "id": "a", "text": "The data appear to demonstrate a modest improvement." },
      { "id": "b", "text": "The data prove an enormous improvement." },
      { "id": "c", "text": "The data unquestionably demonstrate a dramatic improvement." },
      { "id": "d", "text": "The data guarantee a substantial improvement." },
      { "id": "e", "text": "The data establish beyond doubt a complete improvement." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Appear to demonstrate weakens the assertion and signals caution."
  },
  {
    "question": "Which phrase best indicates that a claim is plausible but not certain?",
    "alternatives": [
      { "id": "a", "text": "It is conceivable that" },
      { "id": "b", "text": "It is certain that" },
      { "id": "c", "text": "There is no doubt that" },
      { "id": "d", "text": "It is indisputable that" },
      { "id": "e", "text": "It is beyond question that" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "It is conceivable that introduces a possibility without asserting certainty."
  },
  {
    "question": "Which sentence appropriately qualifies a broad claim?",
    "alternatives": [
      { "id": "a", "text": "In many cases, this strategy appears to produce better outcomes." },
      { "id": "b", "text": "This strategy always produces better outcomes." },
      { "id": "c", "text": "This strategy invariably produces better outcomes." },
      { "id": "d", "text": "This strategy necessarily produces better outcomes." },
      { "id": "e", "text": "This strategy unquestionably produces better outcomes in every situation." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "In many cases and appears to both restrict and soften the claim."
  },
  {
    "question": "Which sentence expresses a cautious disagreement?",
    "alternatives": [
      { "id": "a", "text": "I am not entirely convinced that this interpretation is justified." },
      { "id": "b", "text": "This interpretation is completely absurd." },
      { "id": "c", "text": "This interpretation is unquestionably wrong." },
      { "id": "d", "text": "There is absolutely no merit in this interpretation." },
      { "id": "e", "text": "I categorically reject every aspect of this interpretation." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Not entirely convinced expresses disagreement without making an absolute rejection."
  },
  {
    "question": "Which expression indicates that the writer is making a personal judgment?",
    "alternatives": [
      { "id": "a", "text": "In my view" },
      { "id": "b", "text": "Beyond any doubt" },
      { "id": "c", "text": "Under no circumstances" },
      { "id": "d", "text": "Without exception" },
      { "id": "e", "text": "Invariably" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "In my view explicitly marks the statement as the writer's perspective."
  },
  {
    "question": "Which sentence most appropriately signals that the writer is unsure?",
    "alternatives": [
      { "id": "a", "text": "There is some uncertainty as to whether the measure will succeed." },
      { "id": "b", "text": "The measure will unquestionably succeed." },
      { "id": "c", "text": "The measure is guaranteed to succeed." },
      { "id": "d", "text": "The measure will certainly succeed." },
      { "id": "e", "text": "The measure cannot possibly fail." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Some uncertainty as to whether directly indicates a lack of certainty."
  },
  {
    "question": "Which sentence uses a formal hedge appropriately?",
    "alternatives": [
      { "id": "a", "text": "The available evidence would appear to suggest that further investigation is warranted." },
      { "id": "b", "text": "The evidence definitely proves that further investigation is unnecessary." },
      { "id": "c", "text": "The evidence unquestionably establishes that nothing else needs to be studied." },
      { "id": "d", "text": "The evidence completely rules out the need for further investigation." },
      { "id": "e", "text": "The evidence guarantees that further investigation is pointless." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Would appear to suggest is a formal way of presenting a cautious interpretation."
  },
  {
    "question": "Which sentence expresses moderate confidence?",
    "alternatives": [
      { "id": "a", "text": "The results are likely to reflect a combination of factors." },
      { "id": "b", "text": "The results definitely reflect one specific factor." },
      { "id": "c", "text": "The results unquestionably reflect one specific factor." },
      { "id": "d", "text": "The results certainly reflect one specific factor." },
      { "id": "e", "text": "The results can only reflect one specific factor." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Likely expresses a relatively high degree of probability without certainty."
  },
  {
    "question": "Which sentence expresses low confidence?",
    "alternatives": [
      { "id": "a", "text": "The observed difference might be attributable to sampling error." },
      { "id": "b", "text": "The observed difference is certainly attributable to sampling error." },
      { "id": "c", "text": "The observed difference must be attributable to sampling error." },
      { "id": "d", "text": "The observed difference unquestionably results from sampling error." },
      { "id": "e", "text": "The observed difference definitely results from sampling error." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Might indicates a relatively low level of certainty."
  },
  {
    "question": "Which phrase would best soften a strong criticism?",
    "alternatives": [
      { "id": "a", "text": "Perhaps the most significant weakness is the lack of supporting evidence." },
      { "id": "b", "text": "The most significant weakness is unquestionably the lack of supporting evidence." },
      { "id": "c", "text": "The only serious weakness is definitely the lack of supporting evidence." },
      { "id": "d", "text": "There is absolutely no question that the weakness is the lack of evidence." },
      { "id": "e", "text": "The lack of supporting evidence is undeniably the sole weakness." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Perhaps softens the claim and avoids presenting the judgment as absolute."
  },
  {
    "question": "Which sentence demonstrates appropriate caution when interpreting correlation?",
    "alternatives": [
      { "id": "a", "text": "The correlation may reflect an underlying causal relationship, although this cannot be established conclusively." },
      { "id": "b", "text": "The correlation unquestionably proves causation." },
      { "id": "c", "text": "The correlation definitely establishes a causal relationship." },
      { "id": "d", "text": "The correlation necessarily means that one variable causes the other." },
      { "id": "e", "text": "The correlation completely rules out alternative explanations." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "May reflect and cannot be established conclusively appropriately limit the interpretation."
  },
  {
    "question": "Which sentence expresses a firm stance without sounding excessively absolute?",
    "alternatives": [
      { "id": "a", "text": "There are strong grounds for arguing that the reform should be reconsidered." },
      { "id": "b", "text": "There is absolutely no possible argument against reconsidering the reform." },
      { "id": "c", "text": "Everyone unquestionably agrees that the reform must be abandoned." },
      { "id": "d", "text": "It is impossible for anyone to disagree with this position." },
      { "id": "e", "text": "The reform is obviously wrong in every conceivable respect." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Strong grounds signals a firm but reasoned position without claiming absolute certainty."
  },
  {
    "question": "Which sentence uses a stance adverb to express strong certainty?",
    "alternatives": [
      { "id": "a", "text": "The proposal is undoubtedly worthy of further consideration." },
      { "id": "b", "text": "The proposal is perhaps worthy of further consideration." },
      { "id": "c", "text": "The proposal might be worthy of further consideration." },
      { "id": "d", "text": "The proposal could possibly be worthy of consideration." },
      { "id": "e", "text": "The proposal may potentially be worthy of consideration." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Undoubtedly expresses strong confidence in the statement."
  },
  {
    "question": "Which sentence most effectively avoids categorical language?",
    "alternatives": [
      { "id": "a", "text": "The evidence does not necessarily imply that the intervention was successful." },
      { "id": "b", "text": "The evidence proves that the intervention was successful." },
      { "id": "c", "text": "The evidence unquestionably means that the intervention was successful." },
      { "id": "d", "text": "The evidence inevitably demonstrates success." },
      { "id": "e", "text": "The evidence can only mean that the intervention was successful." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Does not necessarily imply prevents the evidence from being interpreted as conclusive."
  },
  {
    "question": "Which phrase indicates that the writer accepts a possibility but remains cautious?",
    "alternatives": [
      { "id": "a", "text": "It may well be the case that" },
      { "id": "b", "text": "It is unquestionably the case that" },
      { "id": "c", "text": "It is certainly the case that" },
      { "id": "d", "text": "It is indisputably the case that" },
      { "id": "e", "text": "It is beyond doubt that" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "May well be the case that expresses a plausible possibility with moderate confidence."
  },
  {
    "question": "Which sentence appropriately limits the scope of a conclusion?",
    "alternatives": [
      { "id": "a", "text": "These findings are not necessarily representative of the wider population." },
      { "id": "b", "text": "These findings unquestionably represent the entire population." },
      { "id": "c", "text": "These findings are certainly representative of everyone." },
      { "id": "d", "text": "These findings inevitably apply to all populations." },
      { "id": "e", "text": "These findings prove that every group behaves identically." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Not necessarily prevents the findings from being generalized without qualification."
  },
  {
    "question": "Which sentence expresses a carefully qualified opinion?",
    "alternatives": [
      { "id": "a", "text": "On balance, I would argue that the benefits outweigh the drawbacks." },
      { "id": "b", "text": "The benefits unquestionably outweigh every possible drawback." },
      { "id": "c", "text": "There is absolutely no drawback to the proposal." },
      { "id": "d", "text": "Everyone must agree that the benefits outweigh the drawbacks." },
      { "id": "e", "text": "The proposal is obviously beneficial in every respect." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "I would argue and on balance present a reasoned but qualified position."
  },
  {
    "question": "Which sentence expresses skepticism without completely dismissing an argument?",
    "alternatives": [
      { "id": "a", "text": "There is some doubt as to whether the proposed explanation is sufficient." },
      { "id": "b", "text": "The proposed explanation is unquestionably ridiculous." },
      { "id": "c", "text": "The proposed explanation is completely indefensible." },
      { "id": "d", "text": "There is no conceivable merit in the proposed explanation." },
      { "id": "e", "text": "The explanation is categorically unacceptable." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Some doubt expresses skepticism while leaving open the possibility that the explanation has merit."
  },
  {
    "question": "Which expression is most appropriate for cautiously emphasizing an important point?",
    "alternatives": [
      { "id": "a", "text": "It is worth noting that the sample was relatively small." },
      { "id": "b", "text": "It is unquestionably obvious that the sample was completely adequate." },
      { "id": "c", "text": "There is absolutely no reason to consider the sample size." },
      { "id": "d", "text": "The sample size is obviously irrelevant." },
      { "id": "e", "text": "The sample size unquestionably proves the findings." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "It is worth noting highlights a relevant point without making an exaggerated claim."
  },
  {
    "question": "Which sentence uses an appropriate hedge before a prediction?",
    "alternatives": [
      { "id": "a", "text": "The current trend is likely to continue over the coming years." },
      { "id": "b", "text": "The current trend will definitely continue forever." },
      { "id": "c", "text": "The current trend is guaranteed to continue indefinitely." },
      { "id": "d", "text": "The current trend cannot possibly change." },
      { "id": "e", "text": "The current trend will unquestionably continue under all circumstances." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Likely indicates probability rather than certainty."
  },
  {
    "question": "Which sentence expresses a cautious interpretation of unexpected results?",
    "alternatives": [
      { "id": "a", "text": "The unexpected results could perhaps be explained by differences in methodology." },
      { "id": "b", "text": "The unexpected results definitely prove that the methodology was flawed." },
      { "id": "c", "text": "The results unquestionably demonstrate methodological failure." },
      { "id": "d", "text": "The methodology is obviously the only possible explanation." },
      { "id": "e", "text": "The results can only be explained by methodological failure." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could perhaps presents the explanation as a tentative possibility."
  },
  {
    "question": "Which sentence indicates that a claim is based on interpretation rather than direct fact?",
    "alternatives": [
      { "id": "a", "text": "The results could be interpreted as evidence of a gradual decline." },
      { "id": "b", "text": "The results unquestionably prove a gradual decline." },
      { "id": "c", "text": "The results definitely establish a gradual decline." },
      { "id": "d", "text": "The results necessarily demonstrate a gradual decline." },
      { "id": "e", "text": "The results are undeniably evidence of a gradual decline." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could be interpreted explicitly presents the conclusion as an interpretation."
  },
  {
    "question": "Which phrase is most suitable for cautiously presenting a recommendation?",
    "alternatives": [
      { "id": "a", "text": "It might be advisable to reconsider the current strategy." },
      { "id": "b", "text": "It is unquestionably essential to abandon the current strategy." },
      { "id": "c", "text": "The current strategy must definitely be abandoned." },
      { "id": "d", "text": "There is no possible reason to retain the current strategy." },
      { "id": "e", "text": "The current strategy is obviously impossible to defend." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Might be advisable presents the recommendation cautiously."
  },
  {
    "question": "Which sentence expresses a strong but qualified claim?",
    "alternatives": [
      { "id": "a", "text": "The evidence strongly suggests that the current model requires substantial revision." },
      { "id": "b", "text": "The evidence proves beyond any doubt that the model is completely useless." },
      { "id": "c", "text": "The model is unquestionably worthless." },
      { "id": "d", "text": "There is absolutely no reason to retain the model." },
      { "id": "e", "text": "The model is inevitably destined to fail." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Strongly suggests is persuasive but still leaves room for uncertainty."
  },
  {
    "question": "Which sentence appropriately signals that a conclusion is not definitive?",
    "alternatives": [
      { "id": "a", "text": "This conclusion should be regarded as provisional." },
      { "id": "b", "text": "This conclusion is unquestionably definitive." },
      { "id": "c", "text": "This conclusion cannot possibly be challenged." },
      { "id": "d", "text": "This conclusion is beyond all reasonable doubt." },
      { "id": "e", "text": "This conclusion definitively settles the matter." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Provisional explicitly indicates that the conclusion is temporary and open to revision."
  },
  {
    "question": "Which sentence uses cautious language to discuss causation?",
    "alternatives": [
      { "id": "a", "text": "The findings suggest that the intervention may have contributed to the observed improvement." },
      { "id": "b", "text": "The findings prove that the intervention caused the improvement." },
      { "id": "c", "text": "The intervention unquestionably caused the improvement." },
      { "id": "d", "text": "The improvement can only have been caused by the intervention." },
      { "id": "e", "text": "The findings establish causation beyond any doubt." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Suggest and may have contributed both avoid claiming definite causation."
  },
  {
    "question": "Which sentence demonstrates a restrained academic stance?",
    "alternatives": [
      { "id": "a", "text": "While the results are encouraging, they should be interpreted with some caution." },
      { "id": "b", "text": "The results are unquestionably perfect and require no further analysis." },
      { "id": "c", "text": "The results completely settle the issue." },
      { "id": "d", "text": "The results prove that further research is pointless." },
      { "id": "e", "text": "There is absolutely no reason to question the findings." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Interpreted with some caution shows restraint despite acknowledging positive results."
  },
  {
    "question": "Which phrase most clearly indicates a strong degree of probability?",
    "alternatives": [
      { "id": "a", "text": "It is highly likely that" },
      { "id": "b", "text": "It is barely conceivable that" },
      { "id": "c", "text": "It is remotely possible that" },
      { "id": "d", "text": "It is extremely doubtful that" },
      { "id": "e", "text": "It is unlikely that" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Highly likely expresses a strong probability while still allowing for uncertainty."
  },
  {
    "question": "Which sentence indicates that the writer does not fully endorse a previous claim?",
    "alternatives": [
      { "id": "a", "text": "The argument is plausible, although it is not entirely convincing." },
      { "id": "b", "text": "The argument is unquestionably correct in every respect." },
      { "id": "c", "text": "The argument is beyond any possible criticism." },
      { "id": "d", "text": "The argument completely proves the point." },
      { "id": "e", "text": "The argument leaves no room for disagreement." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Plausible acknowledges merit, while not entirely convincing signals reservations."
  },
  {
    "question": "Which sentence appropriately hedges a negative prediction?",
    "alternatives": [
      { "id": "a", "text": "The proposed measures may not be sufficient to address the problem." },
      { "id": "b", "text": "The proposed measures will certainly fail." },
      { "id": "c", "text": "The proposed measures are guaranteed to be ineffective." },
      { "id": "d", "text": "The measures cannot possibly solve the problem." },
      { "id": "e", "text": "The measures will unquestionably make the situation worse." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "May not be sufficient presents the negative prediction as a possibility rather than a certainty."
  },
  {
    "question": "Which expression is best for acknowledging a limitation?",
    "alternatives": [
      { "id": "a", "text": "It should be acknowledged that the study was conducted on a relatively small sample." },
      { "id": "b", "text": "The study unquestionably eliminates every possible limitation." },
      { "id": "c", "text": "The sample size is obviously irrelevant." },
      { "id": "d", "text": "There is no reason whatsoever to consider the sample size." },
      { "id": "e", "text": "The study is completely immune to methodological limitations." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "It should be acknowledged is a formal way to introduce an important qualification."
  },
  {
    "question": "Which sentence presents an opinion with appropriate academic distance?",
    "alternatives": [
      { "id": "a", "text": "It could be argued that the policy has produced unintended effects." },
      { "id": "b", "text": "The policy unquestionably produced unintended effects." },
      { "id": "c", "text": "The policy definitely produced unintended effects." },
      { "id": "d", "text": "There is no possible argument against this conclusion." },
      { "id": "e", "text": "The policy inevitably produced the effects in question." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Could be argued creates distance between the writer and the claim."
  },
  {
    "question": "Which sentence indicates that a claim is only partially supported?",
    "alternatives": [
      { "id": "a", "text": "The evidence lends some support to the hypothesis, but it is far from conclusive." },
      { "id": "b", "text": "The evidence conclusively proves the hypothesis." },
      { "id": "c", "text": "The evidence completely confirms the hypothesis." },
      { "id": "d", "text": "The evidence leaves no doubt whatsoever." },
      { "id": "e", "text": "The hypothesis is unquestionably established." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Some support and far from conclusive clearly indicate limited evidence."
  },
  {
    "question": "Which sentence expresses cautious optimism?",
    "alternatives": [
      { "id": "a", "text": "The initial results are promising, although it remains to be seen whether the trend will continue." },
      { "id": "b", "text": "The initial results guarantee long-term success." },
      { "id": "c", "text": "The initial results unquestionably prove that the strategy will succeed." },
      { "id": "d", "text": "Long-term success is now completely certain." },
      { "id": "e", "text": "There is no possibility that the trend will reverse." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Promising conveys optimism, while it remains to be seen introduces caution."
  },
  {
    "question": "Which sentence uses a hedge to avoid an overly strong conclusion?",
    "alternatives": [
      { "id": "a", "text": "The findings do not appear to provide sufficient evidence for a definitive conclusion." },
      { "id": "b", "text": "The findings definitively establish the correct conclusion." },
      { "id": "c", "text": "The findings unquestionably settle the matter." },
      { "id": "d", "text": "The findings prove that no further research is necessary." },
      { "id": "e", "text": "The findings completely eliminate all uncertainty." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Do not appear to provide avoids treating the findings as conclusive."
  },
  {
    "question": "Which phrase expresses a high degree of confidence while retaining some possibility of error?",
    "alternatives": [
      { "id": "a", "text": "In all likelihood" },
      { "id": "b", "text": "Under no circumstances" },
      { "id": "c", "text": "Beyond any conceivable doubt" },
      { "id": "d", "text": "Without exception" },
      { "id": "e", "text": "Invariably" }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "In all likelihood expresses strong probability without absolute certainty."
  },
  {
    "question": "Which sentence most appropriately expresses a nuanced position?",
    "alternatives": [
      { "id": "a", "text": "Although the proposal has certain merits, its long-term feasibility remains questionable." },
      { "id": "b", "text": "The proposal is either completely successful or completely useless." },
      { "id": "c", "text": "The proposal is unquestionably beneficial in every respect." },
      { "id": "d", "text": "The proposal has no merit whatsoever." },
      { "id": "e", "text": "The proposal is obviously the only viable option." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "The sentence acknowledges strengths while qualifying the proposal's long-term feasibility."
  },
  {
    "question": "Which sentence expresses doubt in a formal way?",
    "alternatives": [
      { "id": "a", "text": "It remains unclear whether the proposed mechanism can account for the observed results." },
      { "id": "b", "text": "The mechanism unquestionably explains all the results." },
      { "id": "c", "text": "The mechanism definitely accounts for the findings." },
      { "id": "d", "text": "The mechanism is obviously the only explanation." },
      { "id": "e", "text": "The mechanism necessarily accounts for every observation." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "It remains unclear formally signals that the answer is still uncertain."
  },
  {
    "question": "Which sentence is most suitable for a cautious academic conclusion?",
    "alternatives": [
      { "id": "a", "text": "Overall, the evidence appears to favor this interpretation, although alternative explanations cannot be ruled out." },
      { "id": "b", "text": "Overall, the evidence completely proves this interpretation." },
      { "id": "c", "text": "Overall, alternative explanations are unquestionably impossible." },
      { "id": "d", "text": "Overall, there is absolutely no reason to question this interpretation." },
      { "id": "e", "text": "Overall, this interpretation is definitively the only possible one." }
    ],
    "correct_answer": "a",
    "level": "c2",
    "content": "hedging and stance (c2)",
    "explanation": "Appears to favor and cannot be ruled out create a cautious and appropriately qualified conclusion."
  }

]

def alt_sig(alts):
    return json.dumps(alts, sort_keys=True, ensure_ascii=False)

with app.app_context():
    created = 0
    skipped = 0

    for q in questions_seed:
        existing = Question.query.filter_by(
            question=q["question"],
            level=q["level"],
            content=q["content"],
            correct_answer=q["correct_answer"],
        ).all()

        duplicate = any(
            alt_sig(e.alternatives) == alt_sig(q["alternatives"])
            for e in existing
        )

        if duplicate:
            skipped += 1
            continue

        db.session.add(Question(**q))
        created += 1

    db.session.commit()
    
    print(f"✅ Seed finalizado. Criadas: {created} | Ignoradas (duplicadas): {skipped}")
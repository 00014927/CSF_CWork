# Final answers for full mark, zero mark and less mark
Complete_answers = {
   "full_mark": "You will get a full mark = 100%",
   "zero_mark": 'Your mark is = 0. ',
   "less_mark": 'You will get below 40 marks minus 10 marks from overall.'
}

# questions and answers == dictionary
Q_ADic = {
    "isSubmissionOnTime": "Did you submit your CW until 1th December?",
    "LateSubmission": "Late Submission!",
    "isSubmissionTooLate": "Did you submit your CW within 24 hours ?",
    "DoYouHaveAGenuineReason": "Do you have a genuine reason ?",
    "ClaimForAnMC": "Claim for an MC...",
    "isSubmissionWithin5Days": "Did you submit within 5 days ?",
    "isThereAGenuineReason": "Is there a genuine reason?",
    "IsThereAValidReason": "Is there a valid reason ?",
    "MCLateSubmissionOption": "MC late submission option!",
    "HasMC(lateSubmissionOptionBeenAccepted": "Has your MC (late submission option) been accepted ?",
    "MCNonSubmissionDeferral": "MC (non-submission deferral) before specified deadline. " "Accepted. " "Deferral "
    "reassessment. ",
    "HasYourClaimForMCBeenAccepted": "Has your Claim for MC been accepted ?",
}

# Question == Deadline of CW
def startQuestions():
    askQuestion(Q_ADic["isSubmissionOnTime"], printFullMark, askSubmissionTooLate)

# CW Submission hours
def askSubmissionTooLate():
    askQuestion(Q_ADic["isSubmissionTooLate"], lateSubmission, askSubmissionWithin5Days)

# CW Submission days
def askSubmissionWithin5Days():
    askQuestion(Q_ADic["isSubmissionWithin5Days"], askQuestion6, askGenuineReason)

# Asking a genuine reason == MC late Submission
def askQuestion6():
    askQuestion(Q_ADic["isThereAGenuineReason"], askReason_MCLateSubmission, markZero)

# Asking a genuine reason = MC Non submission Deferral
def askGenuineReason():
    askQuestion(Q_ADic["IsThereAValidReason"], askReason_MCNonSubmissionDeferral, markZero)

# Ask reason MC non submission defferal
def askReason_MCNonSubmissionDeferral():
    print(Q_ADic["MCNonSubmissionDeferral"])

# Asking MC late submission
def askReason_MCLateSubmission():
    print(Q_ADic["MCLateSubmissionOption"])
    askQuestion(Q_ADic["HasMC(lateSubmissionOptionBeenAccepted"], printFullMark, markZero)

# Printing zero mark
def markZero():
    print(Complete_answers["zero_mark"])

# Printing late submission, and claim an MC, less mark
def lateSubmission():
    print(Q_ADic["LateSubmission"])
    askQuestion(Q_ADic["DoYouHaveAGenuineReason"], claimAnMC, printMarkMinus10)

# Claim an Mc, and getting full mark and less mark
def claimAnMC():
    print(Q_ADic["ClaimForAnMC"])
    askQuestion(Q_ADic["HasYourClaimForMCBeenAccepted"], printFullMark, printMarkMinus10)

# Getting fail
def printFail():
    print("fail")

# Less 10 mark from total mark
def printMarkMinus10():
    print(Complete_answers["less_mark"])

# Getting full mark
def printFullMark():
    print(Complete_answers["full_mark"])

# You can only use yes\ or no\. Otherwise, you cannot continue the program!
def askQuestion(question, conditionYesFn, conditionNoFn):
    answer = input(question)
    if answer == "yes":
        conditionYesFn()
    elif answer == "no":
        conditionNoFn()
    else:
        print("You can only use \"yes\" or \"no\"")
        askQuestion(question, conditionYesFn, conditionNoFn)


startQuestions()



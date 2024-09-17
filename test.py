# import pyghelpers
#
#
# textYesNoDialog(theWindow, theRect, prompt, yesButtonText='Yes',
#  noButtonText='No',
#  backgroundColor=DIALOG_BACKGROUND_COLOR,
#  textColor=DIALOG_BLACK)
#
#
# returnedValue = pyghelpers.textYesNoDialog(window,
#  (75, 100, 500, 150),
#  'Do you want fries with that?')
#
# ignore = pyghelpers.textYesNoDialog(window, (75, 80, 500, 150),
#  'This is an alert!', 'OK', None)
#
# customYesNoDialog(theWindow, oDialogImage, oPromptText, oYesButton,
#  oNoButton)
#
# def showCustomYesNoDialog(theWindow, theText):
#
#
#       oDialogBackground = pygwidgets.Image(theWindow, (60, 120),
#       'images/dialog.png')
#       oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 170),
#       theText, width=WINDOW_WIDTH,
#       justified='center', fontSize=36)
#       oNoButton = pygwidgets.CustomButton(theWindow, (95, 265),
#       'images/noNormal.png',
#       over='images/noOver.png',
#       down='images/noDown.png',
#       disabled='images/noDisabled.png')
#       oYesButton = pygwidgets.CustomButton(theWindow, (355, 265),
#       'images/yesNormal.png',
#       over='images/yesOver.png',
#       down='images/yesDown.png',
#       disabled='images/yesDisabled.png')
#       userAnswer = pyghelpers.customYesNoDialog(theWindow,
#       oDialogBackground,
#       oPromptDisplayText,
#       oYesButton, oNoButton)
#       return userAnswer
#
# textAnswerDialog(theWindow, theRect, prompt, okButtonText='OK'
#  cancelButtonText='Cancel',
#  backgroundColor=DIALOG_BACKGROUND_COLOR,
#  promptTextColor=DIALOG_BLACK,
#  inputTextColor=DIALOG_BLACK)
#
#
# userAnswer = pyghelpers.textAnswerDialog(window, (75, 100, 500, 200),
#  'What is your favorite flavor of ice cream?')
# if userAnswer is not None:
#  # User pressed OK, do whatever you want with the variable userAnswer
# else:
#  # Here do whatever you want knowing that the user pressed Cancel
#
#  def showCustomAnswerDialog(theWindow, theText):
#   oDialogBackground = pygwidgets.Image(theWindow, (60, 80),
#                                        'images/dialog.png')
#   oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 120),
#                                               theText, width=WINDOW_WIDTH,
#                                               justified='center', fontSize=36)
#   oUserInputText = pygwidgets.InputText(theWindow, (225, 165), '',
#                                         fontSize=36, initialFocus=True)
#   oNoButton = pygwidgets.CustomButton(theWindow, (105, 235),
#                                       'images/cancelNormal.png',
#                                       over='images/cancelOver.png',
#                                       down='images/cancelDown.png',
#                                       isabled='images/cancelDisabled.png')
#   oYesButton = pygwidgets.CustomButton(theWindow, (375, 235),
#                                        'images/okNormal.png',
#                                        over='images/okOver.png',
#                                        down='images/okDown.png',
#                                        disabled='images/okDisabled.png')
#   response = pyghelpers.customAnswerDialog(theWindow,
#                                            oDialogBackground, oPromptDisplayText,
#                                            oUserInputText,
#                                            oYesButton, oNoButton)
#   return response
#
#
# userAnswer = showCustomAnswerDialog(window,
#  'What is your favorite flavor of ice cream?')



class mStory(object):
        def showStory(self, label):
            x = 0
            for b in storyList:
                #Look for the right story
                if b.returnLabel() == label:
                   e = 0
                   #show the story if found
                   self.mainSc(x)
                 #No Story found
                else:
                    renpy.say("system","Not returning the right label")
                    renpy.say("system", b.returnLabel())

                x = x + 1

        def make(self, images, transitions, text, choices, choicesText, choicesImages, choicesTransitions, label):
            st = Story(images, transitions, text, choices, choicesText, choicesImages, choicesTransitions, label)

        def mainSc(self, pos):
            e = 0
            for i in storyList[pos].images:
                renpy.scene()
                renpy.show(storyList[pos].images[e])
                if storyList[pos].transitions[e] == 1:
                    renpy.with_statement(dissolve)
                elif storyList[pos].transitions[e] == 2:
                    renpy.with_statement(fade)
                renpy.pause()
                e = e + 1

        def choiceSc(story, pos):
            if(self.choices[pos] == 1):
                e = 0
                for i in story.choicesImages:
                    renpy.scene()
                    renpy.show(storyList[pos].images[e])
                    if story.choicesTransitions[e] == 1:
                        renpy.with_statement(dissolve)
                    elif story.choicesTransitions[e] == 2:
                        renpy.with_statement(fade)
                    renpy.pause()
                    e = e + 1
            else:
                return
    class Story(object):
        def __init__(self, images, transitions, text, choices, choicesText, choicesImages, choicesTransitions, label):
           self.images = images
           self.transitions = transitions
           self.text = text
           self.choices = choices
           self.choicesText = choicesText
           self.choicesImages = choicesImages
           self.choicesTransitions = choicesTransitions

           self.label = label
           storyList.append(self)

        def returnLabel(self):
           return(self.label)

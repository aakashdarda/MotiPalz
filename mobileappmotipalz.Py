from datetime import datetime
import pickle
import random
import time
import math
import tkinter as tk
from tkinter import PhotoImage, font as tkfont, scrolledtext, messagebox
from tkinter import ttk
import os
import tkinter as tk
import webbrowser
import random
 
import tkinter as tk
import webbrowser
import random   # Ensure you have Pillow installed for image handling



class MotiPalzApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MotiPalz")
        self.root.geometry("400x600")
        self.root.configure(bg='black')
        
        self.selected_emoji = None
        self.selected_mood = None
        self.emoji_moods = {
            "😊": ("Happy", "#66ff00"),  # Green for Happy
            "😐": ("Neutral", "#f2e600"),  # Yellow for Neutral
            "😔": ("Sad", "#ff0000"),  # Red for Sad
        }
        # Load custom fonts

         # Tasks for Bingo
        self.tasks = [
            "Eat a fruit", "Exercise", "Meditate", "Drink water", "Read a book",
            "Call a friend", "Stretch", "Write in a journal", "Walk 10 minutes", "Smile",
            "Plan your day", "Declutter", "Cook a meal", "Learn something new", "Do a good deed",
            "Clean a room", "Solve a puzzle", "Take a deep breath", "Hydrate", "Watch the sunset",
            "Plant a seed", "Draw something", "Write a poem", "Organize files", "Dance"
        ]

        # Bingo numbers (1-25)
        self.bingo_numbers = list(range(1, 26))

        # Game state
        self.task_to_bingo = {}
        self.bingo_grid = [[None for _ in range(5)] for _ in range(5)]
        self.completed_tasks = set()
        self.current_task = None

        # Shuffle tasks and numbers
        random.shuffle(self.tasks)
        random.shuffle(self.bingo_numbers)

        # Initialize the game
        self.load_completed_tasks()
        
       
        self.mood_value = tk.IntVar(value=50)
        self.font_big = tkfont.Font(family="Arial", size=16, weight="bold")  # Big font for welcome page
        self.font_normal = tkfont.Font(family="Arial", size=8)
        self.font_mid = tkfont.Font(family="Arial", size=10)  # Normal font for other texts
        self.font_small = tkfont.Font(family="Arial", size=7)  # Smaller font for questions
        self.mood_value = tk.IntVar()
        self.mixer_initialized = False

        self.chapters = [
            {
                "title": "Chapter 1:Atomic Habits by James Clear  ",
                "summary": (
                    "In this chapter, we learn that small changes can lead to remarkable results. "
                    "Atomic habits are the tiny changes we make that compound over time, resulting in significant growth. "
                    "The key is to focus on the system rather than the goal, emphasizing the importance of building "
                    "good habits and breaking bad ones through small, incremental changes."
                ),
            'quiz': [
                
                {
                'question': "1. What are atomic habits?",
                'options': ["A) Large, life-altering changes", "B) Small, incremental habits", "C) Short-lived trends", "D) Random acts of kindness"],
                'correct': 1
            },
            {
                'question': "2. How can small changes impact your life?",
                'options': ["A) They have no effect", "B) They can lead to big transformations", "C) They are always negative", "D) Only large changes matter"],
                'correct': 1
            },
            {
                'question': "3. What is the key focus when building habits?",
                'options': ["A) Setting big goals", "B) Following a strict schedule", "C) Building a system", "D) Getting immediate results"],
                'correct': 2
            },
            {
                'question': "4. What is a system?",
                'options': ["A) A collection of goals", "B) A set of processes", "C) An end result", "D) An occasional task"],
                'correct': 1
            },
            {
                'question': "5. Why are small habits important?",
                'options': ["A) They are easier to maintain", "B) They are less impactful", "C) They take longer to establish", "D) They don’t matter"],
                'correct': 0
            },
                
              ],
            },
            {
             "title":"Chapter 2:  Deep Work by Cal Newport\n",
             "summary":(
                 " Deep Work, Cal Newport explains the concept of deep work—focused, uninterrupted work that leads to high productivity and exceptional results."
                 " He contrasts it with shallow work, which consists of non-essential, often distracting tasks."
                 " Newport argues that in a world full of distractions, the ability to focus deeply is becoming increasingly rare but highly valuable."
                 " The chapter emphasizes how mastering deep work can help individuals achieve extraordinary results in their professional and personal lives."
                 
             ),
             'quiz':[
                  {
                'question': "1. Which of the following best describes deep work?",
                'options': ["A) Working on multiple tasks at once to increase efficiency", "B) Responding to emails and messages quickly to maintain communication", "C)   Performing cognitively demanding tasks in a state of distraction-free focus", "D)  Focusing on administrative and routine tasks"],
                'correct': 2
            },
             {
                'question': "2.  What does Cal Newport identify as the main challenge to engaging in deep work?",
                'options': ["A) A lack of time management skills ", "B) Too much focus on cognitive tasks ", "C)The need to maintain physical health ", "D) The increasing presence of \ndistractions in modern life "],
                'correct': 3
            },
             {
                'question': "3. Why does Cal Newport argue that deep work is becoming increasingly valuable in today’s economy?",
                'options': ["A) Because most jobs require multitasking skills", "B) Because shallow work is no longer relevant in the digital age", "C)  Because the ability to focus deeply is rare\n and leads to high productivity", "D) Because technology eliminates the need for focus"],
                'correct': 2
            },
             {
                'question': "4. Which of the following is an example of shallow work? ",
                'options': ["A) Writing a research paper with full concentration", "B) Responding to routine emails\n and attending unnecessary meetings", "C) Developing a complex algorithm for a software program", "D) Designing a detailed marketing strategy for a new product"],
                'correct': 1
            },
             {
                'question': "5. What does Cal Newport suggest is a primary benefit of practicing deep work?",
                'options': ["A) Increased creativity and ability\n to produce high-quality results", "B) A significant reduction in workload", "C) The ability to multitask effectively", "D) Better communication with colleagues"],
                'correct': 0
            },

             ],
            },     
             {

                "title":"Chapter 3: Getting Things Done by David Allen\n",
             "summary":( "David Allen's Getting Things Done (GTD) is a productivity system designed to overcome procrastination by organizing tasks and minimizing mental clutter."
                          "The system includes five steps: Capture, Clarify, Organize, Reflect, and Engage."
                          "It encourages breaking tasks into actionable steps, maintaining a clear mind, and conducting regular reviews to prioritize effectively."
                           "By providing structure and control, the GTD method helps individuals reduce anxiety, improve focus, and take consistent steps toward their goals." 
                           ),
              'quiz':[
                  {
                'question': "1. What is the primary goal of the GTD system?",
                'options': ["A) Increase workload", "B)  Overcome procrastination and mental clutter", "C) Eliminate unnecessary tasks", "D) Automate daily responsibilities"],
                'correct': 1
            },
             {
                'question': "2.  Which of the following is NOT one of the five steps in the GTD method?",
                'options': ["A)  Capture ", "B)  Reflect ", "C) Engage ", "D) Execute"],
                'correct': 3
            },
             {
                'question': "3. How does the GTD method help reduce anxiety??",
                'options': ["A)By encouraging multitasking ", "B)By breaking tasks into actionable steps", "C) By delegating all tasks to others ", "D)By focusing only on long-term goals "],
                'correct': 1
            },
             {
                'question': "Why does Allen emphasize maintaining a clear mind? ",
                'options': ["A)  To avoid working on multiple tasks", "B)To focus on the task at hand without distraction", "C)  To encourage creativity", "D)  To eliminate the need for regular reviews"],
                'correct': 1
            },
             {
                'question': "5. Who would benefit most from the GTD system?",
                'options': ["A) People with highly automated schedules ", "B)Those who feel bogged down by mental clutter ", "C) Individuals who prefer spontaneous planning ", "D)  People with no long-term goals"],
                'correct': 1
            },              
              ],
            },
        { 
               "title": "Chapter 4:The Power of Habit by Charles Duhigg  ",
  "summary": "The Power of Habit by Charles Duhigg introduces the concept of the habit loop, which consists of three elements: the cue, the routine, and the reward. He explains how habits are formed and how they can be changed. Duhigg emphasizes that understanding the habit loop is essential for both breaking bad habits and cultivating good ones. The chapter also explores how habits work in the brain, with a focus on the basal ganglia, the part of the brain responsible for storing habits.",
  "quiz": [
    {
      "question": "1. What are the three components of the habit loop?",
      "options": [
        "A) Cue, action, reward",
        "B) Motivation, behavior, reward",
        "C) Cue, routine, reward",
        "D) Stimulus, habit, outcome"
      ],
      "correct": 2
    },
    {
      "question": "2. Which part of the brain is primarily responsible for storing habits?",
      "options": [
        "A) Hippocampus",
        "B) Basal ganglia",
        "C) Cortex",
        "D) Amygdala"
      ],
      "correct": 1
    },
    {
      "question": "3. How can bad habits be changed, according to Chapter 1?",
      "options": [
        "A) By eliminating the reward completely",
        "B) By identifying the cue and replacing the routine",
        "C) By focusing only on motivation",
        "D) By waiting for the habit to naturally disappear"
      ],
      "correct": 1
    },
    {
      "question": "4. What is the role of the cue in the habit loop?",
      "options": [
        "A) It is the action that triggers the routine",
        "B) It is the physical reward",
        "C) It is the mental state that encourages the habit",
        "D) It is the environment in which the habit occurs"
      ],
      "correct": 0
    },
    {
      "question": "5. What is the key to successfully changing a habit, according to the chapter?",
      "options": [
        "A) Eliminating all cues associated with the habit",
        "B) Completely avoiding the routine",
        "C) Replacing the routine while keeping the same cue and reward",
        "D) Ignoring the reward and focusing on the cue"
      ],
      "correct": 2
    }
  ]
},
        {
                "title": "Chapter 5: Grit: The Power of Passion and Perseverance by Angela Duckworth",
  "summary": " This book introduces the concept of 'grit' and explains that it is a combination of passion and perseverance for long-term goals. Duckworth emphasizes that talent alone is not enough for success. Instead, it is the consistent effort over time, even in the face of setbacks, that leads to achievement. The chapter also explores how 'showing up' — putting in the effort consistently — is a crucial first step in developing grit.",
  "quiz": [
    {
      "question": "1. What does Angela Duckworth define as grit?",
      "options": [
        "A) A natural talent for success",
        "B) Passion and perseverance for long-term goals",
        "C) A high level of intelligence and skill",
        "D) The ability to take risks"
      ],
      "correct": 1
    },
    {
      "question": "2. According to Duckworth, which of the following is NOT a key component of grit?",
      "options": [
        "A) Passion",
        "B) Perseverance",
        "C) Natural talent",
        "D) Consistency"
      ],
      "correct": 2
    },
    {
      "question": "3. Why does Duckworth believe talent is not enough for success?",
      "options": [
        "A) Because talent can be developed over time",
        "B) Because perseverance and effort are more important for long-term success",
        "C) Because talent alone can lead to complacency",
        "D) Because talent is unreliable"
      ],
      "correct": 1
    },
    {
      "question": "4. What does Duckworth suggest is the most important factor for achieving long-term success?",
      "options": [
        "A) Intelligence",
        "B) Passion and perseverance",
        "C) A strong network",
        "D) Luck"
      ],
      "correct": 1
    },
    {
      "question": "5. According to Duckworth, what is the significance of 'showing up'?",
      "options": [
        "A) It is the first step in achieving long-term goals",
        "B) It guarantees immediate success",
        "C) It helps build natural talent",
        "D) It is more important than passion or perseverance"
      ],
      "correct": 0
    }
  ]
},

        ] 
        self.current_chapter_index = 0
        self.score = 0
        self.lives = 3
        self.total_questions = 5
        self.questions = []
        self.user_answers = []

        self.chapters_extro = [
            {
                "title": "Chapter 1: How to talk to anyone by Leil Lowndes  \n\n",
                "summary": (
            
            "In this chapter, we learn the importance of creating a lasting and positive first impression."
            "Lowndes introduces techniques like the Flooding Smile, which encourages smiling warmly at appropriate moments, and maintaining open, confident body language to exude approachability."
            "The key is to focus on making others feel valued and comfortable from the very first interaction."
            "This chapter illustrates how small adjustments in demeanor can leave a memorable impact on those we meet. "
                ),
            'quiz_extro': [
                
                {
                'question': "1. True or False: The Flooding Smile technique involves smiling constantly to make a good impression.",
                'options': ["A) True", "B) False"],
                'correct': 1
            },
            {
                'question': "2. Which body language tip does Leil Lowndes suggest for creating a positive first impression?",
                'options': ["A) Crossing your arms \nto appear serious", "B) Maintaining open and \nconfident posture", "C) Avoiding eye contact", "D) Standing very still"],
                'correct': 1
            },
            {
                'question': "3. Why does Lowndes emphasize the importance of a Flooding Smile?",
                'options': ["A) To make yourself seem\n overly cheerful", "B) To create a sense of warmth\n and approachability", "C) To distract from nervousness", "D) To appear more professional"],
                'correct': 1
            },
            {
                'question': "4. Scenario: You are meeting someone for the first time. Which of the following actions aligns with Lowndes’ advice?",
                'options': ["A) Smiling warmly and maintaining\n open body language", "B) Looking at your phone\n during introductions", "C) Standing rigidly and\n speaking quickly", "D) Avoiding small talk to get\n straight to the point"],
                'correct': 0
            },
            {
                'question': "5. What is the key benefit of focusing on making others feel valued during a first impression?",
                'options': ["A) It makes the conversation\n more formal.", "B) It helps create a lasting\n and positive connection.", "C) It ensures you dominate\n the interaction.", "D) It avoids the need\n for further small talk."],
                'correct': 1
            },
                
              ],
            },
            {
             "title":"Chapter 2: Crucial Conversations by Kerry Patterson,\n Joseph Grenny, Ron McMillan, and Al Switzler \n",
             "summary":(
                 "Crucial Conversations equips readers with essential tools to navigate high-stakes, emotionally charged discussions with confidence."
                 " It emphasizes the importance of addressing tough conversations to build stronger relationships while avoiding misunderstandings."
                 " Key strategies include staying calm, clarifying intentions, and fostering open dialogue using techniques like mastering your stories to manage emotions."
                 " The STATE method (Share facts, Tell your story, Ask for others' paths, Talk tentatively, Encourage testing) provides a structured framework for tackling sensitive topics constructively, making this book invaluable for improving communication in challenging situations."
                 
             ),
             'quiz_extro':[
                  {
                'question': "1. What is the primary goal of Crucial Conversations?",
                'options': ["A) To teach public speaking skills", "B) To help manage emotionally charged\n discussions effectively", "C)  To promote conflict avoidance", "D) To improve written communication"],
                'correct': 1
            },
             {
                'question': "2.  What does the STATE method stand for?",
                'options': ["A) Stay calm, Take notes,\n Ask questions, Tell stories,\n Encourage listening ", "B) Share facts, Tell your\n story, Ask for others' paths, Talk \ntentatively, Encourage testing ", "C) Speak clearly, Take \ninitiative, Analyze situations, Talk \neffectively, Embrace conflict ", "D) Share truth, \nTell emotions, Ask for advice,\n Take action, Engage openly "],
                'correct': 1
            },
             {
                'question': "3. Which technique helps individuals regulate their emotional responses during difficult conversations?",
                'options': ["A) Encouraging testing", "B) Clarifying intentions", "C) Mastering your stories", "D) Fostering open dialogue"],
                'correct': 2
            },
             {
                'question': "4. Why is it important to address difficult conversations, according to the book? ",
                'options': ["A) To avoid unnecessary confrontation", "B) To improve relationships\n and prevent misunderstandings", "C) To maintain professional decorum", "D) To assert \ndominance in discussions"],
                'correct': 1
            },
             {
                'question': "5. Who would benefit most from reading Crucial Conversations?",
                'options': ["A)  Individuals looking to \nimprove communication in challenging situations", "B) People aiming to \nbecome motivational speakers", "C) Students preparing for academic debates", "D) Authors writing emotional stories"],
                'correct': 0
            },

             ],
            },     
             {

                "title":"Chapter 3: Never Eat Alone by Keith Ferrazzi \n",
             "summary":( "In the first chapter of Never Eat Alone, Keith Ferrazzi emphasizes that building genuine relationships is not about self-interest but about helping others and fostering mutual success."
                          "He introduces the idea of generosity as the foundation for strong networking, encouraging readers to think about what they can give rather than what they can get."
                           "This chapter stresses the importance of authenticity, generosity, and long-term relationship building as essential tools for success." 
                           ),
              'quiz_extro':[
                  {
                'question': "1. What does Keith Ferrazzi suggest is the first step to effective networking?",
                'options': ["A) Attending as many networking events as possible", "B)  Identifying how you can help others", "C) Making a list of people you want to impress", "D) Focusing only on your professional goals"],
                'correct': 1
            },
             {
                'question': "2.  What is the key principle of relationship-building, according to Keith Ferrazzi in Chapter 1?",
                'options': ["A)  Self-promotion and visibility ", "B)  Generosity and helping others ", "C) Creating competitive advantages ", "D)  Avoiding unnecessary interactions"],
                'correct': 1
            },
             {
                'question': "3. How does the GTD method help reduce anxiety??",
                'options': ["A)By encouraging multitasking ", "B)By breaking tasks into actionable steps", "C) By delegating all tasks to others ", "D)By focusing only on long-term goals "],
                'correct': 1
            },
             {
                'question': "4. Ferrazzi believes that genuine networking is rooted in ________. ",
                'options': ["A) Ambition", "B) Patience", "C) Faith  ", "D) Generosity"],
                'correct': 3
            },
             {
                'question': "5.Scenario: You want to connect with a colleague for professional advice. What approach aligns with Ferrazzi’s philosophy?",
                'options': ["A) Immediately ask for help without offering anything in return ", "B)Wait for them to reach out to you ", "C) Research their interests and offer something valuable to them first ", "D) Discuss only work-related topics"],
                'correct': 2
            },              
              ],
            },
        { 
                "title":"Chapter 4: The Like Switch by Jack Schafer\n and Marvin Karlins.\n",
             "summary":(
                 "In this chapter of The Like Switch introduces the concept of the Friend Signal, which is a combination of nonverbal cues used to communicate friendliness and build rapport."
                  "Key elements of the Friend Signal include:"
                  "1) A genuine smile: Shows warmth and approachability."
                  "2) Eyebrow flash: A quick upward movement of the eyebrows that signals recognition and connection."
                  "3) Head tilt: Demonstrates vulnerability and openness."
                  "This chapter emphasizes how these simple yet powerful signals can make you more likable and approachable in both personal and professional settings."
             ),
             'quiz_extro':[
                  {
                'question': "1. What is the main purpose of the Friend Signal?",
                'options': ["A) To demonstrate authority", "B)To assert dominance in a conversation", "C)  To communicate friendliness and build rapport", "D) To establish professional boundaries"],
                'correct': 2
            },
             {
                'question': "2.Why is a genuine smile an important component of the Friend Signal? ",
                'options': ["A) It asserts dominance in\n a social interaction.", "B) It keeps the conversation formal.", "C)   It conveys warmth and approachability.", "D) It ensures you maintain control of the interaction."],
                'correct': 2
            },
             {
                'question': "3.Which of the following is NOT part of the Friend Signal?",
                'options': ["A)Eyebrow flash ", "B) Genuine smile", "C)Head tilt ", "D) Crossed arms "],
                'correct': 3
            },
             {
                'question': "4. What does tilting your head slightly to the side indicate? ",
                'options': ["A)Disinterest in the conversation", "B)Vulnerability and openness", "C) Authority and confidence", "D) A desire to change the topic"],
                'correct': 1
            },
             {
                'question': "5.In which situation would the Friend Signal be most effective?",
                'options': ["A)  When meeting someone for the first time", "B)During a heated argument", "C) While delivering a formal presentation ", "D) When giving instructions to a team"],
                'correct': 0
            }, 
             ],  
            },
        {
  "title": "Chapter 5: Influence: The Psychology of\n Persuasion by Robert Cialdini ",
  "summary": "In this  chapter , Robert Cialdini introduces the concept of 'weapons of influence,' which are psychological triggers used to persuade people. These tactics include reciprocity, commitment, social proof, authority, liking, and scarcity. Cialdini explains how these principles are used by marketers, salespeople, and others to influence human behavior. The chapter emphasizes how understanding these techniques can help individuals recognize and resist manipulative tactics.",
  "quiz_extro": [
    {
      "question": "1. What is the main purpose of the 'weapons of influence'?",
      "options": [
        "A) To promote personal success",
        "B) To manipulate and control others",
        "C) To persuade and influence people's decisions",
        "D) To ensure ethical decision-making"
      ],
      "correct": 2
    },
    {
      "question": "2. Which of the following is NOT one of the 'weapons of influence' discussed in Chapter 1?",
      "options": [
        "A) Reciprocity",
        "B) Commitment",
        "C) Competition",
        "D) Social proof"
      ],
      "correct": 2
    },
    {
      "question": "3. What is the principle of 'reciprocity' in the context of persuasion?",
      "options": [
        "A) Giving something to get something in return",
        "B) Offering discounts to create urgency",
        "C) Following someone's lead to establish credibility",
        "D) Providing unsolicited help to build goodwill"
      ],
      "correct": 0
    },
    {
      "question": "4. According to Cialdini, why are 'weapons of influence' so effective?",
      "options": [
        "A) They appeal to logic and reason",
        "B) They exploit innate human tendencies and biases",
        "C) They rely on clear and transparent communication",
        "D) They are only effective in formal business settings"
      ],
      "correct": 1
    },
    {
      "question": "5. In which situation would the principle of 'social proof' be most effective?",
      "options": [
        "A) When trying to make a difficult decision alone",
        "B) When promoting a new product and using customer reviews",
        "C) When negotiating salary",
        "D) When giving a public speech"
      ],
      "correct": 1
    }
  ]
},

        ] 
        self.current_chapter_index_extro = 0
        self.score_extro = 0
        self.lives_extro = 3
        self.total_questions_extro= 5
        self.questions_extro = []
        self.user_answers_extro = []

        self.chapters_lazy = [
            {
                "title": "Chapter 1: The Now Habit by Neil Fiore",
  "summary": " Neil Fiore introduces the concept of procrastination and explores the psychological reasons behind it. Fiore emphasizes that procrastination is often a response to stress, fear of failure, or perfectionism. The chapter outlines how we can overcome procrastination by shifting our mindset and focusing on positive actions rather than the negative emotions that lead to avoidance. Fiore introduces techniques like the 'unscheduled play' method to reduce stress and foster productivity.",
  "quiz_lazy": [
    {
      "question": "1. What is a common cause of procrastination, according to Neil Fiore?",
      "options": [
        "A) Lack of intelligence",
        "B) Fear of failure and perfectionism",
        "C) Lack of motivation",
        "D) Overcommitment to tasks"
      ],
      "correct": 1
    },
    {
      "question": "2. What technique does Fiore recommend\n for overcoming procrastination?",
      "options": [
        "A) Focusing on the negative outcomes of procrastination",
        "B) Setting long-term goals and deadlines",
        "C) Using the 'unscheduled play' method",
        "D) Delegating tasks to others"
      ],
      "correct": 2
    },
    {
      "question": "3. How does the 'unscheduled play' method help reduce procrastination?",
      "options": [
        "A) It helps to avoid distractions and focus on tasks",
        "B) It encourages relaxation and reduces stress, allowing for better focus",
        "C) It forces individuals to work without taking breaks",
        "D) It provides a reward system for completing tasks"
      ],
      "correct": 1
    },
    {
      "question": "4. Fiore argues that procrastination is primarily a result of what?",
      "options": [
        "A) Poor time management",
        "B) Stress, fear of failure, and perfectionism",
        "C) Lack of goals",
        "D) Lack of self-discipline"
      ],
      "correct": 1
    },
    {
      "question": "5. According to Fiore, what mindset shift is necessary to overcome procrastination?",
      "options": [
        "A) Focusing only on achieving perfection",
        "B) Moving away from fear and guilt and toward positive actions",
        "C) Avoiding any tasks that seem challenging",
        "D) Relying solely on willpower to get things done"
      ],
      "correct": 1
    }
  ]
},
            {
             "title": "Chapter 2: The Procrastination Equation by Piers Steel",
  "summary": "In this chapter of The Procrastination Equation, Piers Steel introduces the scientific understanding of procrastination, exploring its causes and how it impacts people's lives. He presents procrastination as a result of an imbalance between motivation and self-control. Steel explains the 'procrastination equation', which incorporates factors such as expectancy, value, impulsiveness, and delay. The chapter also highlights the emotional and cognitive aspects of procrastination, emphasizing that it's not merely a time management issue, but a psychological one.",
  "quiz_lazy": [
    {
      "question": "1. According to Piers Steel, procrastination is a result of an imbalance between which two factors?",
      "options": [
        "A) Motivation and time management",
        "B) Motivation and self-control",
        "C) Task complexity and emotional response",
        "D) Expectancy and delay"
      ],
      "correct": 1
    },
    {
      "question": "2. What does the 'procrastination equation' take into account?",
      "options": [
        "A) The relationship between reward and task difficulty",
        "B) Expectancy, value, impulsiveness, and delay",
        "C) Time management skills and deadlines",
        "D) Motivation, task goals, and personal relationships"
      ],
      "correct": 1
    },
    {
      "question": "3. Which of the following factors increases the likelihood of procrastination?",
      "options": [
        "A) High expectancy of success",
        "B) High value of the task",
        "C) High impulsiveness and emotional distractions",
        "D) Low delay in task completion"
      ],
      "correct": 2
    },
    {
      "question": "4. How does Piers Steel define procrastination in this chapter?",
      "options": [
        "A) As a time management issue",
        "B) As an emotional and psychological response to tasks",
        "C) As a result of inadequate planning",
        "D) As a lack of self-discipline and focus"
      ],
      "correct": 1
    },
    {
      "question": "5. Which of the following does Steel argue is NOT a direct cause of procrastination?",
      "options": [
        "A) Fear of failure",
        "B) Lack of time management skills",
        "C) Low value of the task",
        "D) Delaying tasks due to impulsiveness"
      ],
      "correct": 1
    }
  ]
},     
             {

                "title": "Chapter 3: Eat That Frog! by Brian Tracy",
  "summary": " Brian Tracy emphasizes the importance of clarity and goal-setting as the first step to overcoming procrastination. He introduces the idea of setting clear, specific goals and prioritizing tasks effectively. Tracy explains that by defining what is most important and creating a detailed plan, individuals can avoid the trap of procrastination. The chapter also emphasizes the importance of personal discipline and commitment to completing tasks on time.",
  "quiz_lazy": [
    {
      "question": "1. According to Brian Tracy, what is the first step in overcoming procrastination?",
      "options": [
        "A) Focusing on smaller tasks first",
        "B) Setting clear and specific goals",
        "C) Increasing motivation",
        "D) Multitasking to get more done"
      ],
      "correct": 1
    },
    {
      "question": "2. What does Tracy mean by setting the table?",
      "options": [
        "A) Organizing your workspace",
        "B) Defining clear goals and priorities",
        "C) Starting with the easiest tasks",
        "D) Creating a to-do list"
      ],
      "correct": 1
    },
    {
      "question": "3. What is the importance of creating a plan according to Tracy?",
      "options": [
        "A) To make tasks seem easier",
        "B) To avoid distractions and focus on priorities",
        "C) To ensure that all tasks are done at once",
        "D) To increase motivation for the hardest tasks"
      ],
      "correct": 1
    },
    {
      "question": "4. What is the main benefit of having clear, specific goals?",
      "options": [
        "A) It helps in measuring success more effectively",
        "B) It reduces the time spent on unimportant tasks",
        "C) It makes tasks feel less challenging",
        "D) It guarantees immediate results"
      ],
      "correct": 1
    },
    {
      "question": "5. Tracy stresses the importance of what quality to achieve success?",
      "options": [
        "A) Procrastination",
        "B) Personal discipline and commitment",
        "C) Avoiding tasks that are difficult",
        "D) Relying on motivation"
      ],
      "correct": 1
    }
  ]
},
        { 
            "title": "Chapter 4: Finish: Give Yourself the Gift\n of Done by Jon Acuff",
  "summary": " Jon Acuff explains that perfectionism is the biggest obstacle to completing goals. He introduces the concept of 'The Day After Perfect,' which refers to the moment when our initial enthusiasm for a goal fades, and perfectionism convinces us to quit. Acuff emphasizes that accepting imperfection and focusing on progress over perfection is key to finishing what we start. The chapter encourages readers to lower the unrealistic standards that often lead to procrastination and self-sabotage.",
  "quiz_lazy": [
    {
      "question": "1. According to Jon Acuff, what is the biggest obstacle to completing goals?",
      "options": [
        "A) Lack of motivation",
        "B) Perfectionism",
        "C) Poor time management",
        "D) External distractions"
      ],
      "correct": 1
    },
    {
      "question": "2. What does The Day After Perfect refer to?",
      "options": [
        "A) The day when you complete your goal",
        "B) The moment when perfectionism convinces you to quit",
        "C) The first day of starting a new goal",
        "D) The day when you plan your next steps"
      ],
      "correct": 1
    },
    {
      "question": "3. What does Acuff suggest is key to finishing what we start?",
      "options": [
        "A) Setting higher goals",
        "B) Lowering unrealistic standards",
        "C) Waiting for the right moment",
        "D) Avoiding any setbacks"
      ],
      "correct": 1
    },
    {
      "question": "4. How does perfectionism lead to procrastination, according to Acuff?",
      "options": [
        "A) By making tasks seem overwhelming and unachievable",
        "B) By encouraging immediate action",
        "C) By increasing focus on small tasks",
        "D) By prioritizing deadlines over quality"
      ],
      "correct": 0
    },
    {
      "question": "5. What mindset does Acuff encourage to achieve success?",
      "options": [
        "A) Focusing on perfection",
        "B) Accepting imperfection and focusing on progress",
        "C) Delaying tasks until you feel ready",
        "D) Striving for flawless execution"
      ],
      "correct": 1
    }
  ]
},
        {
             "title": "Chapter 5: Mindset: The New Psychology of Success by Carol S. Dweck ",
  "summary": " Carol Dweck introduces the two primary types of mindsets: the fixed mindset and the growth mindset. People with a fixed mindset believe their abilities and intelligence are static, which limits their potential. In contrast, those with a growth mindset believe that with effort, learning, and perseverance, they can develop their abilities. Dweck explains how these mindsets shape our behavior, decisions, and ultimately, our success in life. The chapter stresses the importance of cultivating a growth mindset to achieve personal and professional success.",
  "quiz_lazy": [
    {
      "question": "1. What is the key difference between a fixed mindset and a growth mindset?",
      "options": [
        "A) A fixed mindset believes in the ability to grow intelligence, while a growth mindset does not.",
        "B) A fixed mindset believes intelligence is static, while a growth mindset believes abilities can be developed.",
        "C) A growth mindset believes in fixed abilities, while a fixed mindset believes in development.",
        "D) There is no difference between the two mindsets."
      ],
      "correct": 1
    },
    {
      "question": "2. According to Carol Dweck, which mindset leads to greater success in the long term?",
      "options": [
        "A) Fixed mindset",
        "B) Growth mindset",
        "C) Balanced mindset",
        "D) Competitive mindset"
      ],
      "correct": 1
    },
    {
      "question": "3. What happens to people with a fixed mindset when they encounter challenges?",
      "options": [
        "A) They are more likely to persist and learn from mistakes.",
        "B) They avoid challenges and give up easily.",
        "C) They seek out challenges as opportunities to grow.",
        "D) They embrace mistakes as part of the learning process."
      ],
      "correct": 1
    },
    {
      "question": "4. According to Dweck, what is one of the benefits of having a growth mindset?",
      "options": [
        "A) The belief that effort is the key to success.",
        "B) The assumption that abilities are fixed and unchangeable.",
        "C) The focus on immediate results rather than long-term effort.",
        "D) The avoidance of challenges to avoid failure."
      ],
      "correct": 0
    },
    {
      "question": "5. How can one cultivate a growth mindset, according to the chapter?",
      "options": [
        "A) By avoiding mistakes at all costs.",
        "B) By viewing effort and learning as part of the success process.",
        "C) By only focusing on outcomes and results.",
        "D) By believing that talent is the primary factor in success."
      ],
      "correct": 1
    }
  ]
} #above code is just the content for 
  ,

        ] 
        self.current_chapter_index_lazy = 0
        self.score_lazy = 0
        self.lives_lazy = 3
        self.total_questions_lazy = 5
        self.questions_lazy = []
        self.user_answers_lazy = []


        # Sample tasks for the Bingo board
        
        
        # Game state variables
            
        self.show_welcome()  # Start with the welcome page

    def clear_window(self):
        """Clears all widgets in the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome(self):
     """Displays the welcome page."""
     self.clear_window()

     tk.Label(self.root, text="Welcome to MotiPalz :)", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(100, 20))
    
    # Welcome message with automatic text wrapping
     tk.Label(
         self.root,
         text=("Here, every step you take brings you closer to a happier, healthier, and more vibrant you. "
              "Whether it’s building habits, tackling fun challenges, or unlocking the joy of daily wins, "
              "we’re your cheerful companion on this journey. Let’s grow, play, and celebrate life’s little victories "
              "together—because every small effort leads to something extraordinary :) Use this app for a week and it will definately change your life for the good \n - Team MotiPalz"),
         font=self.font_mid,
         fg='#B3E5FC',
         bg='black',
         wraplength=650  # Adjust this value to set the wrapping width
     ).pack(pady=(10,30))

     get_started_button = tk.Button(self.root, text="Get Started !", font=self.font_mid, bg='#66ff00', fg='black',
                                    height=2, width=20, bd=0, relief="flat", command=self.show_menu)
     get_started_button.pack(pady=(10, 30))

     get_started_button.bind("<Enter>", lambda e: get_started_button.config(bg='#009900'))
     get_started_button.bind("<Leave>", lambda e: get_started_button.config(bg='#66ff00'))

    def show_menu(self):
        """Displays the menu page."""
        self.clear_window()

        tk.Label(self.root, text="Choose Your Path to Success <3", font=self.font_big, fg='#66ff00', bg='black', wraplength=700).pack(pady=(50, 20))

        options = ["Become an Extrovert", "Build Habits", "Overcome Laziness"]
        for option in options:
            button = tk.Button(self.root, text=option, font=self.font_big, bg='#66ff00', fg='black', height=3, width=16,
                               bd=0, relief="flat", command=lambda opt=option: self.handle_option(opt))
            button.pack(pady=(100, 60))
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg='#009900'))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg='#66ff00'))

    def handle_option(self, option):
        """Handles the user's selection from the menu."""
        if option == "Build Habits":
            self.show_build_habits(self.current_chapter_index)
        elif option=="Become an Extrovert" :
            self.show_become_extrovert(self.current_chapter_index_extro)
        else:
            self.show_overcome_laziness(self.current_chapter_index_lazy)

    def show_build_habits(self, chapter_index):
        """Displays the Daily Challenge for Building Habits."""
        self.clear_window()
        if chapter_index >= len(self.chapters) or chapter_index < 0:
         messagebox.showerror("Error", "Chapter index out of range!")
         return
        chapter=self.chapters[chapter_index]

        tk.Label(self.root, text="Daily Challenge:", font=self.font_big, fg='#66ff00', bg='black', wraplength=700).pack(pady=(10, 10))
        tk.Label(self.root, text=chapter["title"], font=self.font_big, fg='#66ff00', bg='black', wraplength=700).pack(pady=(10, 10))
        summary_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=35, height=13, bg='black', fg='white', font=self.font_mid)
        summary_box.insert(tk.END, chapter["summary"])
        summary_box.config(state=tk.DISABLED)  # Disable editing
        summary_box.pack(pady=(50, 20))

        # 'I Have Read' button
        read_button = tk.Button(self.root, text="Start Quiz", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.start_chapter_quiz)
        read_button.pack(pady=(10, 20))

        reeaad_button = tk.Button(self.root, text="Next Chapter", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.next_chapter)
        reeaad_button.pack(pady=(10, 20))
        
        reead_button = tk.Button(self.root, text="Back to menu", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.show_menu)
        reead_button.pack(pady=(10, 20))

        read_button.bind("<Enter>", lambda e: read_button.config(bg='#009900'))
        read_button.bind("<Leave>", lambda e: read_button.config(bg='#66ff00'))
        
    def start_chapter_quiz(self):
        """Starts the quiz for the current chapter."""
        chapter=self.chapters[self.current_chapter_index]
        self.questions = chapter['quiz']
        self.current_question_index = 0
        self.total_questions = len(self.questions)
        self.score = 0
        self.lives = 3
        self.show_question()

    def show_question(self):
        """Displays the current question with options."""
        self.clear_window()
        if self.current_question_index >= self.total_questions:
        
         self.show_results()
         return

    # Get the current question data
        question_data = self.questions[self.current_question_index]
        # Display hearts for lives
        heart_display = "<3 " * self.lives  # Show hearts as lives
        tk.Label(self.root, text=heart_display, font=self.font_big, fg='red', bg='black').pack(pady=(100, 10))

        tk.Label(self.root, text=f"Question {self.current_question_index + 1} of {self.total_questions}", font=self.font_mid, fg='#66ff00', bg='black', wraplength=750).pack(pady=(100, 10))

        # Show points
        tk.Label(self.root, text=f"Points: {self.score}", font=self.font_mid, fg='white', bg='black').pack(pady=(50, 10))

        question_data = self.questions[self.current_question_index]
        tk.Label(self.root, text=question_data['question'], font=self.font_mid, fg='white', bg='black', wraplength=750).pack(pady=(10, 20))

        for i, option in enumerate(question_data['options']):
            button = tk.Button(self.root, text=option, font=self.font_normal, bg='#66ff00', fg='black', height=3, width=30,wraplength=750,
                               command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=(10, 10))
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg='#009900'))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg='#66ff00'))

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=800, mode="determinate")
        self.progress_bar.pack(pady=(200, 20))
        self.progress_bar['value'] = (self.current_question_index /self.total_questions) * 100


    def check_answer(self, selected_index):
     """Checks the answer and provides feedback."""
     if selected_index == self.questions[self.current_question_index]['correct']:
         self.score += 1
         messagebox.showinfo("Correct!", "Well done! Your answer is correct.")
         self.current_question_index += 1
         if self.current_question_index < self.total_questions:
             self.progress_bar['value'] = (self.current_question_index / self.total_questions) * 100
             self.show_question()
         else:
             self.show_results()
     else:
         self.lives -= 1  # Deduct a life for incorrect answer
         if self.lives > 0:
             messagebox.showerror("Incorrect!", "Oops! That's not correct. Try again.")
             self.show_question()
         else:
             messagebox.showerror("Game Over!", "You've run out of lives! Returning to the menu.")
             self.show_menu()  # Return to the menu if lives are exhausted


    def show_results(self):
        """Displays the results after completing the questionnaire."""
        self.clear_window()

        tk.Label(self.root, text="Quiz Completed!", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(50, 20))
        tk.Label(self.root, text=f"You scored {self.score} out of {self.total_questions}. \n Give feedback after one week of usage", font=self.font_normal, fg='white', bg='black').pack(pady=(10, 20))

        # Navbar
        self.create_navbar()
    def next_chapter(self):
        """Moves to the next chapter or loops back to the first chapter."""
        self.current_chapter_index += 1
        if self.current_chapter_index >= len(self.chapters):  # Loop back to the first chapter
            self.current_chapter_index = 0
        self.questions = []  # Clear previous questions
        self.score = 0
        self.lives = 3
        self.current_question_index = 0
        self.show_build_habits(self.current_chapter_index)

    def show_become_extrovert(self, chapter_index_extro):
        self.clear_window()
        if chapter_index_extro >= len(self.chapters_extro) or chapter_index_extro < 0:
         messagebox.showerror("Error", "Chapter index out of range!")
         return
        chapter=self.chapters_extro[chapter_index_extro]

        tk.Label(self.root, text="Daily Challenge:", font=self.font_big, fg='#66ff00', bg='black',wraplength=750).pack(pady=(10, 10))
        tk.Label(self.root, text=chapter["title"], font=self.font_big, fg='#66ff00', bg='black',wraplength=750).pack(pady=(10, 10))
        summary_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=35, height=13, bg='black', fg='white', font=self.font_mid)
        summary_box.insert(tk.END, chapter["summary"])
        summary_box.config(state=tk.DISABLED)  # Disable editing
        summary_box.pack(pady=(10, 20))

        # 'I Have Read' button
        read_button = tk.Button(self.root, text="Start Quiz", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.start_chapter_quiz_extro)
        read_button.pack(pady=(10, 20))

        reeaad_button = tk.Button(self.root, text="Next Chapter", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.next_chapter_extro)
        reeaad_button.pack(pady=(10, 20))
        
        reead_button = tk.Button(self.root, text="Back to menu", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.show_menu)
        reead_button.pack(pady=(10, 20))

    
        
    def start_chapter_quiz_extro(self):
        """Starts the quiz for the current chapter."""
        chapter=self.chapters_extro[self.current_chapter_index_extro]
        self.questions_extro = chapter['quiz_extro']
        self.current_question_index_extro = 0
        self.total_questions_extro = len(self.questions_extro)
        self.score_extro = 0
        self.lives_extro = 3
        self.show_question_extro()

    def show_question_extro(self):
        """Displays the current question with options."""
        self.clear_window()
        if self.current_question_index_extro >= self.total_questions_extro:
        
         self.show_results_extro()
         return

    # Get the current question data
        question_data_extro = self.questions_extro[self.current_question_index_extro]
        

        # Display hearts for lives
        heart_display = "<3" * self.lives_extro  # Show hearts as lives
        tk.Label(self.root, text=heart_display, font=self.font_big, fg='red', bg='black').pack(pady=(100, 10))

        tk.Label(self.root, text=f"Question {self.current_question_index_extro + 1} of {self.total_questions_extro}", font=self.font_mid, fg='#66ff00', bg='black').pack(pady=(50, 10))

        # Show points
        tk.Label(self.root, text=f"Points: {self.score_extro}", font=self.font_mid, fg='white', bg='black').pack(pady=(50, 10))

        question_data = self.questions_extro[self.current_question_index_extro]
        tk.Label(self.root, text=question_data_extro['question'], font=self.font_mid, fg='white', bg='black', wraplength=700).pack(pady=(10, 20))

        for i, option in enumerate(question_data_extro['options']):
            button = tk.Button(self.root, text=option, font=self.font_normal, bg='#66ff00', fg='black', height=3, width=30,wraplength=700,
                               command=lambda idx=i: self.check_answer_extro(idx))
            button.pack(pady=(5, 10))
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg='#009900'))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg='#66ff00'))

        # Progress bar
        self.progress_bar_extro = ttk.Progressbar(self.root, orient="horizontal", length=600, mode="determinate")
        self.progress_bar_extro.pack(pady=(50, 20))
        self.progress_bar_extro['value'] = (self.current_question_index_extro /self.total_questions_extro) * 100


    def check_answer_extro(self, selected_index_extro):
     """Checks the answer and provides feedback."""
     if selected_index_extro == self.questions_extro[self.current_question_index_extro]['correct']:
         self.score_extro += 1
         messagebox.showinfo("Correct!", "Well done! Your answer is correct.")
         self.current_question_index_extro += 1
         if self.current_question_index_extro < self.total_questions_extro:
             self.progress_bar_extro['value'] = (self.current_question_index_extro / self.total_questions_extro) * 100
             self.show_question_extro()
         else:
             self.show_results_extro()
     else:
         self.lives_extro-= 1  # Deduct a life for incorrect answer
         if self.lives_extro > 0:
             messagebox.showerror("Incorrect!", "Oops! That's not correct. Try again.")
             self.show_question_extro()
         else:
             messagebox.showerror("Game Over!", "You've run out of lives! Returning to the menu.")
             self.show_menu()  # Return to the menu if lives are exhausted


    def show_results_extro(self):
        """Displays the results after completing the questionnaire."""
        self.clear_window()

        tk.Label(self.root, text="Quiz Completed!", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(50, 20))
        tk.Label(self.root, text=f"You scored {self.score_extro} out of {self.total_questions_extro}.\n Give Feedback after 1 week of usage", font=self.font_normal, fg='white', bg='black').pack(pady=(10, 20))

        # Navbar
        self.create_navbar_extro()
    def next_chapter_extro(self):
        """Moves to the next chapter or loops back to the first chapter."""
        self.current_chapter_index_extro += 1
        if self.current_chapter_index_extro >= len(self.chapters_extro):  # Loop back to the first chapter
            self.current_chapter_index_extro = 0
        self.questions_extro = []  # Clear previous questions
        self.score_extro = 0
        self.lives_extro = 3
        self.current_question_index_extro = 0
        self.show_become_extrovert(self.current_chapter_index_extro)

    def show_overcome_laziness(self, chapter_index_lazy):
        """Displays the Daily Challenge for Building Habits."""
        self.clear_window()
        if chapter_index_lazy >= len(self.chapters_lazy) or chapter_index_lazy < 0:
         messagebox.showerror("Error", "Chapter index out of range!")
         return
        chapter=self.chapters_lazy[chapter_index_lazy]

        tk.Label(self.root, text="Daily Challenge", font=self.font_big, fg='#66ff00', bg='black', wraplength=700).pack(pady=(10, 10))
        tk.Label(self.root, text=chapter["title"], font=self.font_big, fg='#66ff00', bg='black', wraplength=700).pack(pady=(10, 10))
        summary_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=35, height=13, bg='black', fg='white', font=self.font_mid)
        summary_box.insert(tk.END, chapter["summary"])
        summary_box.config(state=tk.DISABLED)  # Disable editing
        summary_box.pack(pady=(10, 20))

        # 'I Have Read' button
        read_button = tk.Button(self.root, text="Start Quiz", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.start_chapter_quiz_lazy)
        read_button.pack(pady=(10, 20))

        reeaad_button = tk.Button(self.root, text="Next Chapter", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.next_chapter_lazy)
        reeaad_button.pack(pady=(10, 20))
        
        reead_button = tk.Button(self.root, text="Back to menu", font=self.font_mid, bg='#66ff00', fg='black',
                                height=2, width=20, bd=0, relief="flat", command=self.show_menu)
        reead_button.pack(pady=(10, 20))

    def start_chapter_quiz_lazy(self):
        """Starts the quiz for the current chapter."""
        chapter=self.chapters_lazy[self.current_chapter_index_lazy]
        self.questions_lazy = chapter['quiz_lazy']
        self.current_question_index_lazy = 0
        self.total_questions_lazy = len(self.questions_lazy)
        self.score_lazy = 0
        self.lives_lazy = 3
        self.show_question_lazy()

    def show_question_lazy(self):
        """Displays the current question with options."""
        self.clear_window()
        if self.current_question_index_lazy >= self.total_questions_lazy:
        
         self.show_results_lazy()
         return

    # Get the current question data
        question_data_lazy = self.questions_lazy[self.current_question_index_lazy]
        # Display hearts for lives
        heart_display = "<3 " * self.lives_lazy  # Show hearts as lives
        tk.Label(self.root, text=heart_display, font=self.font_big, fg='red', bg='black').pack(pady=(100, 10))

        tk.Label(self.root, text=f"Question {self.current_question_index_lazy + 1} of {self.total_questions_lazy}", font=self.font_mid, fg='#66ff00', bg='black').pack(pady=(50, 10))

        # Show points
        tk.Label(self.root, text=f"Points: {self.score}", font=self.font_mid, fg='white', bg='black').pack(pady=(50, 10))

        question_data = self.questions_lazy[self.current_question_index_lazy]
        tk.Label(self.root, text=question_data_lazy['question'], font=self.font_mid, fg='white', bg='black',wraplength=700).pack(pady=(10, 20))

        for i, option in enumerate(question_data['options']):
            button = tk.Button(self.root, text=option, font=self.font_normal, bg='#66ff00', fg='black', height=3, width=30,wraplength=700,
                               command=lambda idx=i: self.check_answer_lazy(idx))
            button.pack(pady=(5, 10))
            button.bind("<Enter>", lambda e, btn=button: btn.config(bg='#009900'))
            button.bind("<Leave>", lambda e, btn=button: btn.config(bg='#66ff00'))

        # Progress bar
        self.progress_bar_lazy = ttk.Progressbar(self.root, orient="horizontal", length=600, mode="determinate")
        self.progress_bar_lazy.pack(pady=(50, 20))
        self.progress_bar_lazy['value'] = (self.current_question_index_lazy /self.total_questions_lazy) * 100


    def check_answer_lazy(self, selected_index_lazy):
     """Checks the answer and provides feedback."""
     if selected_index_lazy == self.questions_lazy[self.current_question_index_lazy]['correct']:
         self.score += 1
         messagebox.showinfo("Correct!", "Well done! Your answer is correct.")
         self.current_question_index_lazy += 1
         if self.current_question_index_lazy < self.total_questions_lazy:
             self.progress_bar_lazy['value'] = (self.current_question_index_lazy / self.total_questions_lazy) * 100
             self.show_question_lazy()
         else:
             self.show_results_lazy()
     else:
         self.lives_lazy -= 1  # Deduct a life for incorrect answer
         if self.lives_lazy > 0:
             messagebox.showerror("Incorrect!", "Oops! That's not correct. Try again.")
             self.show_question_lazy()
         else:
             messagebox.showerror("Game Over!", "You've run out of lives! Returning to the menu.")
             self.show_menu()  # Return to the menu if lives are exhauste
    def show_results_lazy(self):
        """Displays the results after completing the questionnaire."""
        self.clear_window()

        tk.Label(self.root, text="Quiz Completed!", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(50, 20))
        tk.Label(self.root, text=f"You scored {self.score_lazy} out of {self.total_questions_lazy}.\n Give Feedback after 1 week of usage", font=self.font_normal, fg='white', bg='black').pack(pady=(10, 20))
        # Navbar
        self.create_navbar_lazy()
    def next_chapter_lazy(self):
        """Moves to the next chapter or loops back to the first chapter."""
        self.current_chapter_index_lazy += 1
        if self.current_chapter_index_lazy >= len(self.chapters_lazy):  # Loop back to the first chapter
            self.current_chapter_index_lazy = 0
        self.questions_lazy = []  # Clear previous questions
        self.score_lazy = 0
        self.lives_lazy = 3
        self.current_question_index_lazy = 0
        self.show_overcome_laziness(self.current_chapter_index_lazy)

    def create_navbar(self):
     """Creates a navbar at the bottom of the screen."""
     navbar_frame = tk.Frame(self.root, bg='black')
     navbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

     learn_button = tk.Button(navbar_frame, text="Next Chapter", font=self.font_big,
                               bg='#66ff00', fg='black', height=3, width=15,
                             command=self.next_chapter)
     learn_button.pack(side=tk.TOP, pady=(50, 0))  # Increased padding and width

     coming_soon_button = tk.Button(navbar_frame, text="Bingo", font=self.font_big, 
                                    bg='#66ff00', fg='black', height=3, width=15,
                                    command=self.show_bingo)
     coming_soon_button.pack(side=tk.TOP, pady=(50, 0))  # Increased padding and width

     cominng_soon_button = tk.Button(navbar_frame, text="Mood", font=self.font_big,
                                      bg='#66ff00', fg='black', height=3, width=15,
                                   command=self.mood_slider)
     cominng_soon_button.pack(side=tk.TOP, pady=(50, 0))  # Increased padding and width

     tips_button = tk.Button(navbar_frame, text="Feedback", font=self.font_big, 
                             bg='#66ff00', fg='black', height=3, width=15,
                            command=self.feedback)
     tips_button.pack(side=tk.TOP, pady=(50, 0))  # Increased padding and width
     
    def create_navbar_extro(self):
        """Creates a navbar at the bottom of the screen."""
        navbar_frame = tk.Frame(self.root, bg='black')
        navbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

        learn_button = tk.Button(navbar_frame, text="Next Chapter", font=self.font_big, bg='#66ff00', fg='black',
                                  height=3, width=15,
                                 command=self.next_chapter_extro)
        learn_button.pack(side=tk.TOP, pady=(50, 0))

        # summary_button = tk.Button(navbar_frame, text="Summary", font=self.font_normal, bg='#66ff00', fg='black', height=2, width=10,
        #                            command=self.show_summary)
        # summary_button.pack(side=tk.LEFT, padx=(40, 0))

        coming_soon_button = tk.Button(navbar_frame, text="BINGO", font=self.font_big, 
                                       bg='#66ff00', fg='black', height=3, width=15,
                                       command=self.show_bingo)
        coming_soon_button.pack(side=tk.TOP, pady=(50, 0))

        cominng_soon_button = tk.Button(navbar_frame, text="MOOD", font=self.font_big, 
                                        bg='#66ff00', fg='black', height=3, width=15,
                                       command=self.mood_slider)
        cominng_soon_button.pack(side=tk.TOP, pady=(50, 0))

        tips_button = tk.Button(navbar_frame, text="Feedback", font=self.font_big, bg='#66ff00', fg='black',
                                 height=3, width=15,
                                command=self.feedback)
        tips_button.pack(side=tk.TOP, pady=(50, 0))
    def create_navbar_lazy(self):
        """Creates a navbar at the bottom of the screen."""
        navbar_frame = tk.Frame(self.root, bg='black')
        navbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

        learn_button = tk.Button(navbar_frame, text="Next Chapter", font=self.font_big, bg='#66ff00',
                                  fg='black', height=3, width=15,
                                 command=self.next_chapter_lazy)
        learn_button.pack(side=tk.TOP, pady=(50, 0))

        # summary_button = tk.Button(navbar_frame, text="Summary", font=self.font_normal, bg='#66ff00', fg='black', height=2, width=10,
        #                            command=self.show_summary)
        # summary_button.pack(side=tk.LEFT, padx=(40, 0))

        coming_soon_button = tk.Button(navbar_frame, text="BINGO", font=self.font_big,
                                        bg='#66ff00', fg='black', height=3, width=15,
                                       command=self.show_bingo)
        coming_soon_button.pack(side=tk.TOP, pady=(50, 0))

        cominng_soon_button = tk.Button(navbar_frame, text="MOOD", font=self.font_big, 
                                        bg='#66ff00', fg='black', height=3, width=15,
                                       command=self.mood_slider)
        cominng_soon_button.pack(side=tk.TOP, pady=(50, 0))

        tips_button = tk.Button(navbar_frame, text="Feedback", font=self.font_big, 
                                bg='#66ff00', fg='black', height=3, width=15,
                                command=self.feedback)
        tips_button.pack(side=tk.TOP, pady=(50, 0))
        
    def feedback(self):
        """Open a feedback website."""
        url = "https://forms.gle/uy7bWnsz8WsUSD4K7"  
        webbrowser.open(url)
        print(f"Opening: {url}")


    def mood_slider(self):
        """Create Mood Tracker UI with emojis and a confirm button."""
        self.clear_window()

        # Title
        tk.Label(
            self.root,
            text="How Are You Feeling Today?",
            font=self.font_big,
            fg="#66ff00",
            bg="black",
            wraplength=700
        ).pack(pady=(50, 10))

        # Emojis
        emojis = [(":) ", "Happy"), (":| ", "Neutral"), (":(", "Sad"),]
        self.emoji_buttons = []

        # Create emoji buttons
        frame = tk.Frame(self.root, bg="black")
        frame.pack(pady=(50, 0))

        for emoji, mood in emojis:
            btn = tk.Label(
                frame,
                text=emoji,
                font=("Arial", 50),
                fg="white",
                bg="black",
                cursor="hand2",
            )
            btn.mood = mood  # Store mood info
            btn.bind("<Enter>", self.on_hover)  # Hover effect
            btn.bind("<Leave>", self.on_leave)  # Leave hover effect
            btn.bind("<Button-1>", self.on_click)  # Click effect
            btn.pack(side="left", padx=20)
            self.emoji_buttons.append(btn)

        # Confirm Button centered
        confirm_btn = tk.Button(
            self.root,
            text="Confirm Mood",
            font=self.font_big,
            bg="#66ff00",
            fg="black",
            height=2,
            width=15,
            command=self.show_sub_options,
        )
        confirm_btn.pack(pady=(200, 10))  # Centering with padding

    def clear_window(self):
        """Clear the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_hover(self, event):
        """Highlight emoji on hover."""
        event.widget.config(fg="#66ff00")

    def on_leave(self, event):
        """Remove hover highlight."""
        if self.selected_emoji != event.widget:
            event.widget.config(fg="white")

    def on_click(self, event):
        """Select or deselect an emoji."""
        # Deselect previous selection
        if self.selected_emoji:
            self.selected_emoji.config(fg="white", bg="black")

        # Highlight current selection
        self.selected_emoji = event.widget
        self.selected_mood = self.selected_emoji.mood

        # Update color based on the selected mood
        mood_color = {"Happy": "#66FF00", "Neutral": "#FFD700", "Sad": "#FF0000", "Frustrated": "#FF0000"}.get(self.selected_mood, "black")
        self.selected_emoji.config(fg="black", bg=mood_color)

    def show_sub_options(self):
        """Show sub-options based on selected mood."""
        if not self.selected_mood:
            return  # Do nothing if no emoji selected

        # Determine mood text and options
        if self.selected_mood == "Happy":
            mood_text = "You're feeling Happy :) "
            options = ["Lets Dance", "Stay Happy", "Listen to a Happy Song"]
        elif self.selected_mood == "Neutral":
            mood_text = "You're feeling Neutral :| "
            options = ["Lets meditate", "Take a break", "Relaxing song"]
        else:  # Sad
            mood_text = "You're feeling Sad :("
            options = ["Need Motivation?", "Watch Cartoon", "Lets get happy"]

        # Clear window for sub-options
        self.clear_window()

        # Show selected mood message
        tk.Label(self.root, text=mood_text, font=self.font_big, fg="white", bg="black",wraplength=600).pack(pady=(20, 10))

        # Display each sub-option as a button
        for option in options:
            tk.Button(self.root, text=option, font=self.font_mid, bg="#66ff00", fg="black",
                      height=3, width=30, wraplength=600, command=lambda opt=option: self.show_suggestion(opt)).pack(pady=(50, 10))
            
             # Back button
        tk.Button(self.root, text="Back", font=self.font_small, bg="red", fg="white",
                  command=self.show_congrats).pack(pady=(30, 10))

    def show_suggestion(self, option):
     """Show personalized suggestions for the selected sub-option."""
     # Define suggestion content for each sub-option with multiple links
     suggestions = {
          "Lets Dance": {
             "text": "Form a routine :)",
             "video": ["https://www.youtube.com/watch?v=oGneAab3e88","https://www.youtube.com/watch?v=2yeRRm9AIxI","https://www.youtube.com/watch?v=i0AUEswUayo", "https://youtu.be/LK7-_dgAVQE?si=diIa7sOTNh2l8JjM"]
        },
         "Stay Happy": {
             "text": "Stand up and smile :)",
             "video": ["https://youtu.be/oQ98C_8ATQY?si=TJFHxSaLGLCeXvA1","https://youtu.be/jaMEkbILo2Q?si=7HtW0X9_w_yl0B9b", "https://youtu.be/2Zskkd3bb9A?si=J6BMxXdfeUgtWQOJ","https://youtu.be/5EFTzkb6jho?si=-xVmYs_19Usjb-dE"]
        },
         "Listen to a Happy Song": {
             "text": "Here is a song to lift your mood :)",
             "video": ["https://www.youtube.com/watch?v=6w67NOaRe-w&list=RD-z_UvHknyrc&index=9","https://www.youtube.com/watch?v=-z_UvHknyrc","https://www.youtube.com/watch?v=TpMSsbzvRe4&list=PL8U7gDbfLksNOQ-IbN_jfC9DVQYt4xXTo&index=13", "https://www.youtube.com/watch?v=dx4Teh-nv3A&list=PL406sb8c3_OkjFTgwKb8SX-ul1tChD6Hr"]
        },
         "Lets meditate": {
             "text": "Sit down and meditate for 5 minutes: ",
             "video": ["https://youtu.be/inpok4MKVLM?si=V_b3MfmlZiEByT1f", "https://www.youtube.com/watch?v=zSkFFW--Ma0"]
        },
         "Take a break": {
             "text": "Here’s a 5-minute stretching video to help you relax: ",
             "video": ["https://youtu.be/sAf67xFS-qE?si=hlRTZjDqaNOi-k7p", "https://youtu.be/2L2lnxIcNmo"]
        },
         "Relaxing song": {
            "text": "Here is a calming melody :)",
            "video": ["https://www.youtube.com/watch?v=HCWvgoTfUjg","https://www.youtube.com/watch?v=ZmcBC9-wAXM&list=RDZmcBC9-wAXM", "https://www.youtube.com/watch?v=hoNb6HuNmU0"]
        },
        "Need Motivation?": {
            "text": "Watch this motivational video to get inspired: ",
            "video": ["https://youtu.be/9dsjGQnl4H0?si=A9B94e77rfjJMgWE","https://www.youtube.com/watch?v=IHwqhSLE9Gc","https://youtu.be/_HEnohs6yYw?si=iDFe8VuWQ2yDJcda", "https://www.youtube.com/watch?v=75d_29QWELk"]
        },
        "Watch Cartoon": {
            "text": "Relax and smile :)",
            "video": ["https://www.youtube.com/watch?v=yR1wbqGz06c", "https://youtu.be/_3L36d9JKvI?si=oC88w1h9JL1Ux86U"]
        },
        "Lets get happy": {
            "text": "Here is a happy tune for you :)",
            "video": ["https://www.youtube.com/watch?v=6w67NOaRe-w&list=RD-z_UvHknyrc&index=9","https://www.youtube.com/watch?v=-z_UvHknyrc","https://www.youtube.com/watch?v=TpMSsbzvRe4&list=PL8U7gDbfLksNOQ-IbN_jfC9DVQYt4xXTo&index=13", "https://www.youtube.com/watch?v=dx4Teh-nv3A&list=PL406sb8c3_OkjFTgwKb8SX-ul1tChD6Hr"]
        },
    }

    # Get the suggestion based on the option
     if option in suggestions:
        suggestion = suggestions[option]
        # Pick a random video link
        random_video = random.choice(suggestion["video"])
        
        # Display suggestion text
        print(suggestion["text"])  # Replace this with UI logic to display the text in your app

        # Open the random video link in a web browser
        webbrowser.open(random_video)
     else:
        print("No suggestion found for the selected option!")  # Handle invalid options

       # Back button
        tk.Button(self.root, text="Back", font=self.font_small, bg="red", fg="white",
                  command=self.show_congrats).pack(pady=(30, 10))

    def show_congrats(self):
     """Displays the congratulations page after the questionnaire."""
     self.clear_window()

    # Display the congratulations message and score
     tk.Label(self.root, text="Congratulations!", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(50, 20))
     tk.Label(self.root, text=f"You scored {self.score} out of {self.total_questions}.", font=self.font_normal, fg='white', bg='black').pack(pady=(10, 20))

    # Create the navbar
     self.create_navbar() 

    def show_bingo(self):
        """Sets up the Bingo game."""
        self.clear_window()

        # Title
        tk.Label(self.root, text="Bingo Game", font=self.font_big, fg='#66ff00', bg='black').pack(pady=10)

        # Center frame for Bingo grid
        center_frame = tk.Frame(self.root, bg='black')
        center_frame.pack(pady=10)

        # Populate Bingo grid
        if not self.bingo_grid[0][0]:
            for i in range(5):
                for j in range(5):
                    number = self.bingo_numbers[i * 5 + j]
                    task = self.tasks.pop(0)
                    self.task_to_bingo[task] = (i, j)

                    label = tk.Label(
                        center_frame, text=number, font=self.font_normal, width=5, height=2,
                        bg='white', fg='black', relief="raised", bd=2
                    )
                    label.grid(row=i, column=j, padx=5, pady=5)
                    self.bingo_grid[i][j] = label

        # Update Bingo grid colors based on completed tasks
        for task, (i, j) in self.task_to_bingo.items():
            if task in self.completed_tasks:
                self.bingo_grid[i][j].config(bg='green')

        # Show the default task (if no task is active)
        if not self.current_task:
            self.current_task = random.choice(list(self.task_to_bingo.keys()))

        # Current task display
        self.task_label = tk.Label(
            self.root, text=f"Task: {self.current_task}",
            font=self.font_normal, fg='white', bg='black'
        )
        self.task_label.pack(pady=5)

        # Buttons section
        button_frame = tk.Frame(self.root, bg='black')
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Task Done", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.complete_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame, text="Back", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.show_congrats
        ).grid(row=0, column=1, padx=5)

    def complete_task(self):
        """Completes the current task and updates the Bingo grid."""
        if not self.current_task:
            return

        # Mark the task as completed
        i, j = self.task_to_bingo[self.current_task]
        self.bingo_grid[i][j].config(bg='green')
        self.completed_tasks.add(self.current_task)

        # Check for a Bingo line after completing the task
        if self.check_bingo():
            self.show_congrats()
            return

        # Pick a new task
        remaining_tasks = set(self.task_to_bingo.keys()) - self.completed_tasks
        if remaining_tasks:
            self.current_task = random.choice(list(remaining_tasks))
            self.task_label.config(text=f"Task: {self.current_task}")
        else:
            self.task_label.config(text="All tasks completed!")

        # Save progress
        self.save_completed_tasks()

    def show_bingo(self):
        """Sets up the Bingo game."""
        self.clear_window()

        # Title
        tk.Label(self.root, text="Bingo Game", font=self.font_big, fg='#66ff00', bg='black').pack(pady=10)

        # Center frame for Bingo grid
        center_frame = tk.Frame(self.root, bg='black')
        center_frame.pack(pady=10)

        # Populate Bingo grid
        if not self.bingo_grid[0][0]:
            for i in range(5):
                for j in range(5):
                    number = self.bingo_numbers[i * 5 + j]
                    task = self.tasks.pop(0)
                    self.task_to_bingo[task] = (i, j)

                    label = tk.Label(
                        center_frame, text=number, font=self.font_normal, width=5, height=2,
                        bg='white', fg='black', relief="raised", bd=2
                    )
                    label.grid(row=i, column=j, padx=5, pady=5)
                    self.bingo_grid[i][j] = label

        # Update Bingo grid colors based on completed tasks
        for task, (i, j) in self.task_to_bingo.items():
            if task in self.completed_tasks:
                self.bingo_grid[i][j].config(bg='green')

        # Show the default task (if no task is active)
        if not self.current_task:
            self.current_task = random.choice(list(self.task_to_bingo.keys()))

        # Current task display
        self.task_label = tk.Label(
            self.root, text=f"Task: {self.current_task}",
            font=self.font_normal, fg='white', bg='black'
        )
        self.task_label.pack(pady=5)

        # Buttons section
        button_frame = tk.Frame(self.root, bg='black')
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Task Done", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.complete_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame, text="Back", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.show_congrats
        ).grid(row=0, column=1, padx=5)

    def complete_task(self):
        """Completes the current task and updates the Bingo grid."""
        if not self.current_task:
            return

        # Mark the task as completed
        i, j = self.task_to_bingo[self.current_task]
        self.bingo_grid[i][j].config(bg='green')
        self.completed_tasks.add(self.current_task)

        # Check for completed lines
        self.check_bingo()

        # Pick a new task
        remaining_tasks = set(self.task_to_bingo.keys()) - self.completed_tasks
        if remaining_tasks:
            self.current_task = random.choice(list(remaining_tasks))
            self.task_label.config(text=f"Task: {self.current_task}")
        else:
            self.task_label.config(text="All tasks completed!")

        # Save progress
        self.save_completed_tasks()

    def show_bingo(self):
        """Sets up the Bingo game."""
        self.clear_window()

        # Title
        tk.Label(self.root, text="Bingo Game", font=self.font_big, fg='#66ff00', bg='black').pack(pady=10)

        # Center frame for Bingo grid
        center_frame = tk.Frame(self.root, bg='black')
        center_frame.pack(pady=10)

        # Populate Bingo grid
        if not self.bingo_grid[0][0]:
            for i in range(5):
                for j in range(5):
                    number = self.bingo_numbers[i * 5 + j]
                    task = self.tasks.pop(0)
                    self.task_to_bingo[task] = (i, j)

                    label = tk.Label(
                        center_frame, text=number, font=self.font_mid, width=5, height=3,
                        bg='white', fg='black', relief="raised", bd=2
                    )
                    label.grid(row=i, column=j, padx=5, pady=5)
                    self.bingo_grid[i][j] = label

        # Update Bingo grid colors based on completed tasks
        for task, (i, j) in self.task_to_bingo.items():
            if task in self.completed_tasks:
                self.bingo_grid[i][j].config(bg='green')

        # Show the default task (if no task is active)
        if not self.current_task:
            self.current_task = random.choice(list(self.task_to_bingo.keys()))

        # Current task display
        self.task_label = tk.Label(
            self.root, text=f"Task: {self.current_task}",
            font=self.font_normal, fg='white', bg='black'
        )
        self.task_label.pack(pady=5)

        # Buttons section
        button_frame = tk.Frame(self.root, bg='black')
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Task Done", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.complete_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame, text="Back", font=self.font_normal, bg='#66ff00', fg='black', width=12,
            command=self.show_congrats
        ).grid(row=0, column=1, padx=5)

    def complete_task(self):
        """Completes the current task and updates the Bingo grid."""
        if not self.current_task:
            return

        # Mark the task as completed
        i, j = self.task_to_bingo[self.current_task]
        self.bingo_grid[i][j].config(bg='green')
        self.completed_tasks.add(self.current_task)

        # Check for completed lines
        self.check_bingo()

        # Pick a new task
        remaining_tasks = set(self.task_to_bingo.keys()) - self.completed_tasks
        if remaining_tasks:
            self.current_task = random.choice(list(remaining_tasks))
            self.task_label.config(text=f"Task: {self.current_task}")
        else:
            self.task_label.config(text="All tasks completed!")

        # Save progress
        self.save_completed_tasks()

    def check_bingo(self):
        """Checks if there is a completed line in the Bingo grid."""
        for i in range(5):
            # Check if all cells in the row are green or yellow
            if all(self.bingo_grid[i][j].cget("bg") in ['green', 'yellow'] for j in range(5)):
                self.highlight_line(row=i)

            # Check if all cells in the column are green or yellow
            if all(self.bingo_grid[j][i].cget("bg") in ['green', 'yellow'] for j in range(5)):
                self.highlight_line(column=i)

        # Check diagonals
        if all(self.bingo_grid[i][i].cget("bg") in ['green', 'yellow'] for i in range(5)):
            self.highlight_line(diagonal="main")
        if all(self.bingo_grid[i][4 - i].cget("bg") in ['green', 'yellow'] for i in range(5)):
            self.highlight_line(diagonal="anti")

    def highlight_line(self, row=None, column=None, diagonal=None):
        """Highlights a completed line in yellow."""
        if row is not None:
            for j in range(5):
                self.bingo_grid[row][j].config(bg='yellow')
        elif column is not None:
            for i in range(5):
                self.bingo_grid[i][column].config(bg='yellow')
        elif diagonal == "main":
            for i in range(5):
                self.bingo_grid[i][i].config(bg='yellow')
        elif diagonal == "anti":
            for i in range(5):
                self.bingo_grid[i][4 - i].config(bg='yellow')

    def show_congrats(self):
        """Displays a congratulations screen."""
        self.clear_window()
        tk.Label(self.root, text="Congratulations!", font=self.font_big, fg='white', bg='black').pack(pady=20)
        tk.Label(self.root, text="You've completed a Bingo line!", font=self.font_normal, fg='white', bg='black').pack(pady=10)
        tk.Button(
            self.root, text="Back to Bingo", font=self.font_normal, bg='#66ff00', fg='black', command=self.show_bingo
        ).pack(pady=10)

    def save_completed_tasks(self):
        """Saves the completed tasks to a file."""
        with open('completed_tasks.pkl', 'wb') as file:
            pickle.dump({'completed_tasks': self.completed_tasks}, file)

    def load_completed_tasks(self):
        """Loads the completed tasks from a file."""
        try:
            with open('completed_tasks.pkl', 'rb') as file:
                data = pickle.load(file)
                self.completed_tasks = data.get('completed_tasks', set())
        except FileNotFoundError:
            self.completed_tasks = set()
    def show_congrats(self):
     """Displays the congratulations page after the questionnaire."""
     self.clear_window()

    # Display the congratulations message and score
     tk.Label(self.root, text="Congratulations!", font=self.font_big, fg='#66ff00', bg='black').pack(pady=(50, 20))
     tk.Label(self.root, text=f"You scored {self.score} out of {self.total_questions}.", font=self.font_normal, fg='white', bg='black').pack(pady=(10, 20))

    # Create the navbar
     self.create_navbar()

if __name__ == "__main__":
    root = tk.Tk()
    app = MotiPalzApp(root)
    root.mainloop()


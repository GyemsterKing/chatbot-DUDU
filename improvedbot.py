import datetime
import random
# All DETAILS OF COLLEGES AND DATA

general_questions={ 'name':["They call me DUDU, but you can call me 'the knowledge genie'.",
                            "You can call me whatever you like, but my official name is DUDU.",
                            "I'm still figuring out my identity, but for now, you can call me DUDU.",
                            "You can call me DUDU.",
                            "I'm DUDU your friendly AI assistant.",
                            "I go by the name of DUDU."
                               ],
                        'else_responses':["I'm not sure about that. Why don't you try searching on Google?",
                                          "That's a great question! I'm still learning, so I can't answer that yet.",
                                          "Let's try a different question. How about asking me about colleges?",
                                          "I'm not equipped to answer that right now. Perhaps you could rephrase your question?"
                                          ],
                        'hi_responses':["Hi! How can I help you today?",
                                        "Hello! What would you like to ask?",
                                        "Hi there! Feel free to ask me anything.",
                                        "Hey! What's up? How can I assist you?",
                                        "Hello! Ready to chat? Ask away!",
                                        "Greetings! How can I be of service?",
                                        "Yo, what's crackin'? Need a hand?",
                                        ],

                        'goodbye_messages':["Goodbye! Have a nice day.",
                                            "See you later! Feel free to ask any more questions.",
                                            "Thanks for chatting. Bye!",
                                            "Bye for now!",
                                            "Have a wonderful day! Until next time.",
                                            "Take care! Remember, I'm always here if you need me.",
                                            "Peace out! Catch you on the flip side.",
                                        ],

                        'tips' :{'exams':["Understand the Syllabus",
                                          "Build a Strong Foundation",
                                          "Practice Regularly",
                                          "Time Management",
                                          "Join a Reputed Coaching Institute",
                                          "Take Mock Tests",
                                          "Stay Healthy and Manage Stress",
                                          "Seek Guidance",
                                          "Stay Updated",
                                          "Believe in Yourself"],
                                 'physics' : ["Understand concepts", 
                                                  "Practice numerical problems", 
                                                  "Visualize concepts", 
                                                  "Join study groups"],
                                 'chemistry' : ["Understand theory", 
                                                     "Practice numerical problems", 
                                                     "Learn periodic table", 
                                                     "Do experiments"],
                                 'maths' : ["Practice regularly", 
                                                 "Understand concepts", 
                                                 "Practice previous year papers", 
                                                 "Use formula book"],
                                 'biology' : ["Understand concepts",
                                                   "Practice diagrams", 
                                                   "Read textbooks", 
                                                   "Solve MCQs"]
                                                   }
                                
                }
top_engineering_colleges = {
        "IIT Madras": "1. Indian Institute of Technology Madras",
        "IIT Delhi": "2. Indian Institute of Technology Delhi",
        "IIT Bombay": "3. Indian Institute of Technology Bombay",
        "IIT Kanpur": "4. Indian Institute of Technology Kanpur",
        "IIT Kharagpur": "5. Indian Institute of Technology Kharagpur",
        "IIT Roorkee": "6. Indian Institute of Technology Roorkee",
        "IIT Guwahati": "7. Indian Institute of Technology Guwahati",
        "IIT Hyderabad": "8. Indian Institute of Technology Hyderabad",
        "NIT Trichy": "9. National Institute of Technology Tiruchirappalli",
        "VIT": "10. Vellore Institute of Technology"
}                      
top_medical_colleges ={
        "AIIMS Delhi": "1. All India Institute of Medical Sciences, Delhi",
        "CMC Vellore": "2. Christian Medical College, Vellore",
        "AFMC": "3. Armed Forces Medical College, Pune",
        "BHU": "4. Banaras Hindu University",
        "Amrita Vishwa Vidyapeetham": "5. Amrita Vishwa Vidyapeetham",
        "D Y Patil": "6. D. Y. Patil Vidyapeeth",
        "SRM Institute": "7. S.R.M. Institute of Science and Technology",
        "Siksha 'O' Anusandhan": "8. Siksha 'O' Anusandhan University",
        "MAMC": "9. Maulana Azad Medical College",
        "Lady Hardinge": "10. Lady Hardinge Medical College"
}
top_colleges_by_state = {
    "maharashtra": ["VIT Pune", "DY Patil University", "Symbiosis Institute of Technology", "KJ Somaiya College of Engineering"],
    "uttar pradesh": ["AKTU Colleges", "IMS Engineering College", "KGMC"],
    "rajasthan": ["MNIT Jaipur", "JECRC University", "Jaipur National University", "SMS Medical College"],
    "delhi": ["DTU", "NSUT", "IIIT Delhi", "AIIMS Delhi", "MAMC"],
    "uttarakhand": ["Uttarakhand Technical University", "Doon Medical College", "IIT Roorkee"]
}
degree_info = {
        "dpharma": {
            "fees": 100000,
            "duration": 2,
            "future_fields":["1. Consultant Pharmacists", 
                              "2. Clinical Pharmacist", 
                              "3. Dispensary Manager", 
                              "4. Dispensary Pharmacist", 
                              "5. Community Pharmacist",
                            
                                ]
            },
        "bams": {
            "fees": 250000,
            "duration": 5.5,
            "future_fields": ["1. Medical transcription",
                              "2. Medical tourism", 
                              "3. Medical event management", 
                              "4. Medical journalism", 
                              "5. Medical photography and documentation"
                                ]
            },
        "mbbs": {
            "fees": 1500000,
            "duration": 5,
            "future_fields":["1. Public Health\n",
                             "2. Medical Research\n",
                             "3. Medical Education\n",
                             "4. Medical Administration\n",
                             "5. Medical Writing and Journalism\n",
                             ]


            },
        "llb": {
            "fees": 750000,
            "duration": 5,  
            "future_fields": ["Corporate Law\n",
                              "Criminal Law\n",
                              "Civil Law\n",
                              "IP Law\n"]

           },


        "btech": {  
        "fees": 800000, 
        "duration": 4,
        "future_fields": ["Computer Science and Engineering\n",
                            "Mechanical Engineering\n",
                            "Electrical Engineering\n",
                            "Civil Engineering\n",
                            "Chemical Engineering\n",
                            "Biotechnology\n",
            "Electronics and Communication Engineering\n",
            "Information Technology\n", ]


        },
  
        }
degree_eligibility ={
            "btech": {
                "Education":"10+2 with Physics, Chemistry, and Mathematics",
                "Minimum aggregate percentage": "Varies by college and state",
                "Entrance exams": "JEE Main, JEE Advanced (for IITs), state-level engineering exams"
            },
            "mbbs": {
                "Education":"10+2 with Physics, Chemistry, and Biology",
                "Minimum aggregate percentage": "Varies by state and medical college",
                "Entrance exams": "NEET-UG"
                },
            "bca": {
                "Education":"10+2 with Mathematics",
                "Minimum aggregate percentage": "Varies by college and university"
                },
            "mba": {
                "Education":"Bachelor's degree in any discipline",
                "Minimum aggregate percentage": "Varies by college and university",
                "Entrance exams": "CAT, GMAT, XAT, MAT, CMAT"
                }
            }
colleges_eligiblity = {
        "iit madras": {
            "Name": "Indian Institute of Technology Madras",
            "Eligibility": "10+2 with Physics, Chemistry and Mathematics (JEE Advanced qualified)",
            "Location": "Chennai, Tamil Nadu",
            "Website": "https://www.iitm.ac.in/"
            },
        "iit delhi": {
            "Name": "Indian Institute of Technology Delhi",
            "Eligibility": "10+2 with Physics, Chemistry and Mathematics (JEE Advanced qualified)",
            "Location": "New Delhi",
            "Website": "https://www.iitd.ac.in/"
            },
        "iit bombay": {
            "Name": "Indian Institute of Technology Bombay",
            "Eligibility": "10+2 with Physics, Chemistry and Mathematics (JEE Advanced qualified)",
            "Location": "Mumbai, Maharashtra",
            "Website": "https://www.iitb.ac.in/"
            },
        "aiims delhi": {
            "Name": "All India Institute of Medical Sciences, Delhi",
            "Eligibility": "10+2 with Physics, Chemistry and Biology (NEET-UG qualified)",
            "Location": "New Delhi",
            "Website": "https://aiims.edu/"
            },
        "cmc vellore": {
            "Name": "Christian Medical College, Vellore",
            "Eligibility": "10+2 with Physics, Chemistry, and Biology (NEET-UG qualified)",
            "Location": "Vellore, Tamil Nadu",
            "Website": "https://www.cmcvellore.ac.in/"
            },
        "iit kanpur": {
            "Name": "Indian Institute of Technology Kanpur",
            "Eligibility": "10+2 with Physics, Chemistry, and Mathematics (JEE Advanced qualified)",
            "Location": "Kanpur, Uttar Pradesh",
            "Website": "https://www.iitk.ac.in/"
            },
        "iit kharagpur": {
            "Name": "Indian Institute of Technology Kharagpur",
            "Eligibility": "10+2 with Physics, Chemistry, and Mathematics (JEE Advanced qualified)",
            "Location": "Kharagpur, West Bengal",
            "Website": "https://www.iitkgp.ac.in/"
            },
        "iit roorkee": {
            "Name": "Indian Institute of Technology Roorkee",
            "Eligibility": "10+2 with Physics, Chemistry, and Mathematics (JEE Advanced qualified)",
            "Location": "Roorkee, Uttarakhand",
            "Website": "https://www.iitr.ac.in/"
            }
        
    }
keyword={'keywords_help' : ['help', 'stuck', 'confused'],
         'keywords_greetings' : ['hii','hey', 'hello', 'how are you', 'hlo'],
         'keywords_eligibility' : ['eligibility', 'criteria'],
         'keywords_tips': ['tips', 'preparation', 'strategy', 'guide', 'exam tip'],
         'keywords_states':['delhi','rajasthan','uttarakhand','maharashtra','uttar pradesh'],
         'keyword_career':['future','options','career','job'],
         'keyword_name':['introduce','yourself','name','call you'],
         'keyword_extra':['done','thank','ok'],
         'extra':["I hope that helps!",
                  "Let me know if you have any other questions."]
       }



def eligibility_code():
    degree_or_college = input("Bot: Enter Degree or College for Eligiblity Info: ").lower()

    if degree_or_college in degree_eligibility:

        print("Bot: Here is the info as you want")
        print('')
        print('Education: ',degree_eligibility[degree_or_college]['Education'])
        print('Minimum Aggregate Percentage: ',degree_eligibility[degree_or_college]['Minimum aggregate percentage'])
        print('Entrance Exams: ',degree_eligibility[degree_or_college]['Entrance exams'])
        print('')
        print("\nSource: nirfindia.org \n shiksha.com")
        

    elif degree_or_college in colleges_eligiblity:

        print("Bot: Here is the info as you want")
        print('')
        print("Eligibility: ",colleges_eligiblity[degree_or_college]['Eligibility'])
        print('Location: ',colleges_eligiblity[degree_or_college]['Location'])
        print('Website: ',colleges_eligiblity[degree_or_college]['Website'])
        print('')
        print("\nSource: nirfindia.org \n shiksha.com")
                
        
    else:

        print("Bot: I couldn't find specific information. Please try rephrasing your query or asking something else.")
        else_websites()
def get_degree_info(degree):
        if degree in degree_info:
            info = degree_info[degree]
            print("Bot: Great choice....wanna know more about it")
            print('')
            inpu=input("You: ").lower()
            if 'y' in inpu:
                print("Bot: Here's some information about ",degree.upper())
                print('')
                print("Fees: ",info['fees'])
                print("Duration: ",info['duration'] ,"years")
                print("\nSource: coursera.org \n bestcolleges.com \n shiksha.com")
                for ctr in info['future_fields']:
                    print(ctr)
                    continue
            else:
                print("Bot: OK ... :-) :-) ")
        else:
            print("Bot:Great Choice....But Currently We're not carrying more info about this")
def else_websites():
        print("Here are some resources that might be helpful:")
        print("- CollegeDunia")
        print("- Shiksha")
def learn_from_user(response):
    general_questions[user_input] = response

    # ASLI TEHELKA STARTS FROM HERE
learn=[]


current_time = datetime.datetime.now()
if current_time.hour <= 12:
    greeting = "Good Morning"
elif current_time.hour >=12 and current_time.hour <=18:
    greeting = "Good Afternoon"
else:
    greeting = "Good evening"
print("Bot: ",greeting,", Buddy!")


# ACTUAL CODE STARTS
while True:
        user_input = input("You: ").lower()
        print('')

        #GENERAL QUESTIONS
        if any(key in user_input for key in keyword['keywords_help']):
            print("Bot: You can ask me about colleges, degrees, or any other related queries.")
            continue
        if 'menu' in user_input:
            print("Bot: Here's a menu of what I can help you with:\n"
                "1. Find colleges\n"
                "2. Get information about degrees\n"
                "3. Ask general questions\n")
            continue
        if any(key in user_input for key in keyword["keyword_name"]):
            print('Bot: ',random.choice(general_questions['name']))
            continue
        if any(key in user_input for key in keyword["keywords_greetings"]):
            gender = input("How would you like me to address you? (Male/Female/Other): ").lower()
            if 'f' in gender:
                print("Bot: Hello, Sir! How can I help you today?")
            elif 'm' in gender:
                print("Bot: Hello, Ma'am! How can I help you today?")
            else:
                print("Bot: Hello! How can I help you today?")
            continue
        # QUESTION 1
        for ctr in top_colleges_by_state:
            if ctr in user_input:
                if 'college' in user_input or 'university' in user_input or 'institute' in user_input:
                    for g in top_colleges_by_state[ctr]:
                        print(g)
                    continue
                else:
                    print("Bot: Sorry didn't understand what you want to know about ",ctr )
                    continue
        

        # QUESTION 2
        if 'college' in user_input or 'university' in user_input:
            print("Bot: Are you interested in pursuing a career in engineering, medical, or another field?")
            print('')
            field = input("You: ").lower()
                 

            # Medical college
            
            if 'bio' in field or 'medi' in field:
                print("Bot: These could be some top medical colleges you can pursue:")
                print('')
                print("\nSource: nirfindia.org \n shiksha.com")
                for cc in top_medical_colleges:
                    print(top_medical_colleges[cc])
                    
                print('')
                print('')
                print("Bot: Which degree do you want to pursue?")
                print('')
                degree = input("You: ").lower()
                get_degree_info(degree)
                continue
                    

            # Engineering college
            elif 'iit' in field or 'engineering' in field or 'btech' in field:
                print("Bot: Here are some of the top engineering colleges you can consider pursuing:")
                print('')
                print("\nSource: nirfindia.org \n shiksha.com")
                for cc in top_engineering_colleges:
                    print(top_engineering_colleges[cc])
                print('')
                print('')
                print("Bot: Which degree do you want to pursue?")
                print('')
                degree = input("You: ").lower()
                get_degree_info(degree)
                continue

            else:
                print("Bot: Sorry, I don't have information about that field.")
                continue

        # QUESTION 3
        if 'eligibility' in user_input or 'criteria' in user_input:
            eligibility_code()
            continue

        # QUESTION 4
        if any(key in user_input for key in keyword["keywords_tips"]):
            for ctr in general_questions["tips"]['exams']:
                print(ctr)
            print('')
            continue
           
        # QUESTION 5
        for a in degree_info:
            if ('job' in user_input or 'career' in user_input or 'options' in user_input) and a in user_input:
                for ctr in degree_info:
                    if ctr in user_input:
                        for a in degree_info[ctr]['future_fields']:
                            print(a)
            
        # QUESTION 6   
        if any(key in user_input for key in keyword["keyword_career"]):
            interest = input("Bot: What field are you interested in? (e.g., engineering, medicine): ")
            if 'engi' in interest:
                print("Consider these fields: \n\nComputer Science\n Mechanical Engineering\n Electrical Engineering\n Civil Engineering\n")
            elif 'medi' in interest:
                print("Consider these fields:\n\n MBBS\n BDS\n BAMS\n BHMS\n")
            else:
                print("Bot: I don't deal in this field")
            continue
        
        # QUESTION 7 
        if 'how to study' in user_input or 'study tips' in user_input:
            subject=input("Bot: Which subject would you like tips for?").lower()
            for ctr in general_questions['tips'][subject]:
                print(ctr)
            continue    
        
        # QUESTION 8
        if any(key in user_input for key in keyword["keyword_extra"]):
            print(random.choice(keyword['extra'])) 
            continue

        # QUESTION 9
        

            continue
        # END STATEMENT
        if user_input in learn:
            print('Bot: ',general_questions[user_input])
            
        if 'exit' in user_input or 'see you' in user_input or 'by' in user_input:
            print("Bot: ",random.choice(general_questions['goodbye_messages']))
            break
            
        else:
            if user_input not in learn:
                print("Bot: I don't know the answer to that. Can you please provide more information?")
                response = input("You: ")
                learn_from_user(response)
                learn.append(user_input)
                print("Bot: Thank you for teaching me. I'll remember that.")
                
            
                 
        
            




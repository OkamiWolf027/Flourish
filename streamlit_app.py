import streamlit as st
import mental_health as mh
from replit import db

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Symptoms", "Personalized Coping Mechanisms", "Self Care", "What you did daily", "Find What Works For You"])

with tab1:
  st.title("Flourish")
  st.write("A healthy way of coping with mental health issues.")
  #Home screen
  st.header("What Flourish Does")
  st.write("Coping with mental health issues can be hard, but Flourish can help! Recieve customized reccomendations based on your menthal health needs, or see everything we have to offer!")

  
with tab2:
  st.title("Different Mental Health Symptoms")
  st.write("Different disorders present themselves differently. If you don't know what to do, or what you think you're suffering from, read about different symptoms here!")
  inpu1=st.radio("Click a disorder to see the Symptoms associated with it.",mh.get_disorder_list(),index=None)
  if(inpu1!=None):
    st.write(mh.symptoms[inpu1])

with tab3:
  st.title("Personalized Coping Mechanisms")
  st.write("Different conditions require different treatments.")
#A spot where someone can get mechanisms tailored to their specific disorder
  inpu1=st.radio("What mental disorder are you struggling with?",mh.get_disorder_list(),index=None)
  if(inpu1!=None):
    inpu2=st.radio("Here are some healthy coping methods.",mh.remove_parentheses(mh.disorder[inpu1]),index=None,help="Click on the coping method to learn more about it.",key=2)
    if(inpu2!=None):
      st.write(mh.cope[mh.add_parentheses(inpu2,inpu1)],index=None)

with tab4:
  st.title("Self Care")
  st.write("Struggling with mental health issues may be hard, but always make time to take care of yourself! It can be very beneficial to you in the long run.")
  inpu1=st.radio("What self care methods do you want to learn about?",["Hygiene","Pets","Entertainment","Food","Hobbies"],index=None)
  if(inpu1=="Hygiene"):
    st.write("Try taking a long bath. Take care of your skin, and keep it clean and healthy by doing a skincare routine! It will make you feel refreshed and relaxed, and much more motivated!")
  elif(inpu1=="Pets"):
    st.write("Spending time with pets is an amazing way to relieve stress and anxiety, as well as other mental illnesses! Petting animals can prove very beneficial and calming. And as a bonus, your cute fluffy buddy will thank you for the attention! Snuggling/Petting animals is a great way to combat mental illnesses. ")
  elif(inpu1=="Entertainment"):
    st.write("Watching/reading your favorite show, movie, or book is a great way to combat mental illnesses. It can help to distract your mind when you’re feeling down and be used as a countermeasure to taking drugs or alcohol!")
  elif(inpu1=="Food"):
    st.write("Eating delicious foods is one of the many great things to live for. Tasting things you like releases dopamine into your brain and makes you happy! Eating too much can prove troublesome, but eating healthy with an occasional sweet won’t hurt!")
  elif(inpu1=="Hobbies"):
    st.write("Having hobbies is one of the best ways to combat mental illnesses. It distracts your mind from feeling sad and lets you have fun and be happy! Take up, for example, drawing, cooking, writing, crocheting, or athletics. There are so many different hobbies that can make you so special and unique! Enjoy the things life gives you.")

with tab5:
  st.title("What you did daily")

  st.write("Select the Self Care methods you used today")
  goals=db["goals"]
  daily=[False]*len(goals)
  count=0
  for x in goals:
    daily[count] = st.checkbox(x)
    count+=1
  if(st.button("Submit")):
    comp_daily=0
    comp = db["completed"]
    for x in daily:
      if x:
        comp_daily+=1
        comp+=1
    st.write("you completed: "+str(comp_daily)+" of your daily goals today")
    st.write("you have completed: "+str(comp)+" of your daily goals")
    db["completed"]=comp
  add=st.text_input("Add new goal")
  if(st.button("Add")):
    db["goals"].append(add)
    st.write("added: " + add)
  rem=st.text_input("Remove goal")
  if(st.button("Remove")):
    if(rem in goals):
      db["goals"].remove(rem)
      st.write("removed: " + rem)
    else:
      st.write("there is no goal called: " + rem)
    st.write("reload the site to see the new goals")

with tab6:
  st.title("Full List of Coping Mechanisms")
  st.write("Here is a full list of mechanisms that can help when coping with mental health issues.")
  st.write("Following some of these can still be benifitial even if you don't have a that mental disorder (As long as it's not taking medicine: you should not do that unless perscribed by a doctor).")
  st.write("Above all else, we reccomend that you talk to someone. It can help you relieve some of the built up stress and they can help you manage your condition. Talk to someone you trust, they will want to help you!")
  #a spot where people can just see any mechanism that we have
  inpu1=st.radio("Here are some healthy coping methods",mh.get_cope_list(True),index=None,help="Click on the coping method to learn more about it.",key=1)
  if(inpu1!=None):
    st.write(mh.cope[inpu1],index=None)

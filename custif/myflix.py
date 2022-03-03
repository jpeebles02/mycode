#!/usr/bin/env python3
position = input("Chose a position between Quater Back, Wide Reciever, or Running Back")
if position.lower() == "quater back":
  print("you chose", position)
if position.lower() == "wide reciever":
  print("you chose", position)
if position.lower() == "running back":
  print("you chose", position)
  weight = int(input("What is your weight"))
  if weight >= 250:
    message = 'Unfortunately you cannot run the ball. It would be unfair to the defense'
  elif weight <= 249:
    message = 'You are eligible to run the ball'
  print(message)

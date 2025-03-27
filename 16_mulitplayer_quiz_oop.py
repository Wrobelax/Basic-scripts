"""A Multi-Player Quiz using several OOP techniques."""

from typing import List


class Player:
    def __init__(self, name) -> None:
        self.name = name.title()
        self.score = 0


class Question:
    def __init__(self, prompt:str, answer: str) -> None:
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions: List[Question]) -> None:
        self.questions = questions
        self.players_list = []


    def add_player(self, player:Player) -> None:
        self.players_list.append(player)


    def ask_question(self) -> str:
        for player in self.players_list:
            print(f"\nTurn to {player.name}")
            for question in self.questions:
                answer = input(question.prompt)
                if answer.lower() == question.answer.lower():
                    player.score += 1
            print(f"\nPlayer {player.name} finished with a score of {player.score}.")


    def show_winner(self) -> str:
        winner = max(self.players_list, key= lambda p:p.score)
        print(f"\nWinner is {winner.name} with a score of {winner.score} points.")


# Questions and answers
questions = [
    Question("What is the capital of Poland? ", "Warsaw"),
    Question("What is 2+2? ", "4"),
    Question("What does a monkey eat? ", "Banana")
]


# Create players
player_1 = Player(input("Enter Player 1 name:"))
player_2 = Player(input("Enter Player 2 name:"))


# Create a quiz
quiz = Quiz(questions)


# Append players
quiz.add_player(player_1)
quiz.add_player(player_2)

# Ask questions and show the winner
quiz.ask_question()
quiz.show_winner()
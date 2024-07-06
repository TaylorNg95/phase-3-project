from helpers import exit_program, clear_screen
from models.match import Match
from models.opponent import Opponent
""" import ipdb """

class Cli:

    def run(self):
        clear_screen()
        print('WELCOME TO YOUR MATCH LOG!')
        self.options()

    def options(self):
        print('')
        print('Type "1" to view all matches')
        print('Type "2" to add new match')
        print('Type "3" to delete existing match')
        print('Type "4" to view all opponents')
        print('Type "5" to add new opponent')
        print('Type "6" to delete existing opponent')
        print('Type "7" to search matches by opponent')
        print('Type "8" to search matches by date')
        print('Type "exit" to exit program')
        print('')
        self.selection()

    def selection(self):
        sel = input('Enter selection: ')
        clear_screen()
        if sel == '1':
            self.view_all_matches()
        elif sel == '2':
            self.add_new_match()
        elif sel == '3':
            self.delete_existing_match()
        elif sel == '4':
            self.view_all_opponents()
        elif sel == '5':
            self.add_new_opponent()
        elif sel == '6':
            self.delete_existing_opponent()
        elif sel == '7':
            self.matches_by_opponent()
        elif sel == '8':
            self.matches_by_date()
        elif sel.lower() == 'exit':
            exit_program()
        else:
            print('Invalid input. Please try again!')
            print('')
            self.options()

    def view_all_matches(self):
        all_matches = [value for key, value in Match.all.items()]
        print('ALL MATCHES:')
        print('')
        for match in all_matches:
            # adjust spacing to ensure alignment depending on ID length
            spacing = '  '
            if 10 <= match.id < 100:
                spacing = ' '
            elif 100 <= match.id < 1000:
                spacing = ''
            print(f'ID: {match.id}{spacing}| DATE: {match.date} | OUTCOME: {"W" if match.outcome == 1 else "L"} | OPPONENT: {match.opponent_id}')
            print('------')
        self.options()

    def add_new_match(self):
        """ print('ADDING NEW MATCH:')
        print('')
        print('In order to add a new match, you must know the opponent ID.')
        print('Type "1" to proceed')
        print('Type "2" to view all opponents')
        print('Type "3" to create new opponent') """
        pass

    def delete_existing_match(self):
        pass

    def view_all_opponents(self):
        all_opponents = [value for key, value in Opponent.all.items()]
        print('ALL OPPONENTS:')
        print('')
        for opponent in all_opponents:
            # adjust spacing to ensure alignment depending on ID length
            spacing = '  '
            if 10 <= opponent.id < 100:
                spacing = ' '
            elif 100 <= opponent.id < 1000:
                spacing = ''
            print(f'ID: {opponent.id}{spacing}| {opponent.name}')
            print('------')
        self.options()

    def add_new_opponent(self):
        pass

    def delete_existing_opponent(self):
        pass

    def matches_by_opponent(self):
        pass

    def matches_by_date(self):
        pass
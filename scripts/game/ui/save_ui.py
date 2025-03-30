from scripts.game.save_system import Profile, SaveSystem
from scripts.game.ui.main_dashboard import MainDashboard
from scripts.game.ui.ui_node import UINode


class SaveUI(UINode):
    def __init__(self, parent=None, options=None):
        super().__init__("Save Game", parent, options)
        profiles = SaveSystem.get_profiles()
        if profiles:
            self.options = list(profiles.values())
        else:
            self.options = []
        self.profile = None # last profile created

    def draw_ui(self, message=None):
        self.options = list(SaveSystem.get_profiles().values())
        _message = f"Dear Warrior, you want to save your game? You are at the right place."
        super().draw_ui(_message)
        print(f"Enter the option number...............         or New Profile[n] | Delete Profile[x] | Go Back[b]")
        self.process_input(["n", "x", "b"])

    def process_input(self, valid_options):
        super().process_input(valid_options)

    def custom_valid_options(self, input_option):
        if not super().custom_valid_options(input_option):
            if input_option == "n":
                self.new_profile()
            if input_option == "x":
                self.delete_profile()
    
    def index_selection(self, index):
        # Just want to save no need to follow super that just moves to the next node.
        if index >= len(self.options):
            self.main()
            return
        profile = self.options[index]
        SaveSystem.save(profile.display_text, {})  # TODO - SaveObject Dict and Saving functionality.
        MainDashboard.push_notification(f"Game saved to profile {profile.display_text.title()}!")
        self.main()
        

    def clear_input(self):
        super().clear_input()

    def delete_profile(self):
        try:
            profile_index = int(input("Enter the number of the profile you want to delete: \n>>> "))
            if profile_index >= len(self.options):
                MainDashboard.push_notification(f"Unable to delete profile... Index out of bounds!")
                self.remain()
                return
            profile_name = self.options[profile_index - 1].display_text
            SaveSystem.remove_profile(profile_name)
            self.options = list(SaveSystem.get_profiles().values())
            MainDashboard.push_notification(f"Save Profile \"{profile_name}\" deleted!")
        except ...:
            MainDashboard.push_notification(f"Unable to delete profile... Incorrect option selected!")
        finally:
            self.remain()

    def new_profile(self):
        profile_name = input("Enter new profile name then strike the enter key to save your game in the new profile: \n>>> ")
        SaveSystem.add_profile(Profile(profile_name))
        SaveSystem.save(profile_name, {})  # TODO - SaveObject Dict and Saving functionality.
        MainDashboard.push_notification(f"Game saved to new profile {profile_name.title()}!")
        # Re-fetch profiles to ensure consistency
        self.options = list(SaveSystem.get_profiles().values())
        self.main()

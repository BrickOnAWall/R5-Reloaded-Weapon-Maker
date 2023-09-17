#Importing PyQt5, and system
import sys, webbrowser, os
from PyQt5.QtWidgets import QFileDialog, QRadioButton, QTreeWidgetItem, QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QPushButton, QListWidget, QLineEdit, QToolBar, QMenuBar, QMessageBox, QMenu, QMessageBox, QTableWidget, QTreeWidget, QTableWidgetItem, QAbstractItemView, QAbstractScrollArea, QAbstractItemView



#Create new instance of Tab
class Tab1(QWidget):
    def __init__(self):

        alternator = "mp_weapon_alternator_smg"
        charge_Rifle = "mp_weapon_defender"
        devotion = "mp_weapon_esaw"
        epg = "mp_weapon_epg"
        eva = "mp_weapon_shotgun"
        flatline = "mp_weapon_vinson"
        g7 = "mp_weapon_g2"
        havoc = "mp_weapon_energy_ar"
        hemlok = "mp_weapon_hemlok"
        kraber = "mp_weapon_sniper"
        longbow = "mp_weapon_dmr"
        lstar = "mp_weapon_lstar"
        mastiff = "mp_weapon_mastiff"
        mozambique = "mp_weapon_shotgun_pistol"
        p2020 = "mp_weapon_semipistol"
        peacekeeper = "mp_weapon_energy_shotgun"
        prowler = "mp_weapon_pdw"
        r301 = "mp_weapon_rspn101"
        r99 = "mp_weapon_r97"
        re45 = "mp_weapon_autopistol"
        smart_pistol = "mp_weapon_smart_pistol"
        spitfire = "mp_weapon_lmg"
        triple_take = "mp_weapon_doubletake"
        wingman = "mp_weapon_wingman"
        
        
        common_names = ["alternator", "charge_Rifle", "devotion", 
                        "eva", "flatline", "g7", "havoc", "hemlok", "kraber",
                        "longbow", "lstar", "mastiff", "mozambique","p2020",
                        "peacekeeper", "prowler", "r301", "r99", "re45", 
                        "spitfire", "triple_take", "wingman"]

        rifles = [flatline, havoc, hemlok, lstar, r301, spitfire, devotion]
        shotguns = [eva, peacekeeper, mozambique, mastiff]
        pistols = [p2020, re45, wingman]
        smgs = [alternator, prowler, r99]
        snipers = [triple_take, longbow, kraber, g7, charge_Rifle]

        settings_menu = QMenu("Settings")
        
        super().__init__()
        layout = QVBoxLayout()

        #Create a title
        title = QLabel("Weapon Info: ")
        title.setStyleSheet("font: bold;")
        layout.addWidget(title)

        #Create weapon name input
        global weapon_name
        weapon_name = QLineEdit()
        weapon_name.setPlaceholderText("Weapon Name")
        layout.addWidget(weapon_name)
        
        #Create weapon description input
        global weapon_description
        weapon_description = QLineEdit()
        weapon_description.setPlaceholderText("Weapon Description")
        layout.addWidget(weapon_description)


        #Create a label
        model_list = QLabel("Model Selection: ")
        model_list.setStyleSheet("font: bold;")
        layout.addWidget(model_list)

        #Create a tree table including the weapon categories
        global weapon_tree
        weapon_tree = QTreeWidget()
        weapon_tree.setHeaderLabels(["Model Type:", "Model Name:", "Common Name:"])
        weapon_tree.setColumnWidth(0, 100)
        
        #Create style sheet for tree table
        weapon_tree.setStyleSheet("height:125px")
        weapon_tree.setAlternatingRowColors(True)
        weapon_tree.setSelectionBehavior(QAbstractItemView.SelectRows)
        weapon_tree.setSelectionMode(QAbstractItemView.SingleSelection)

        #Add weapons to correct tree table column
        weaponss = {
            "RIFLE": rifles,
            "SHOTGUN": shotguns,
            "SNIPER": snipers,
            "PISTOL": pistols,
            "SMG": smgs
        }
        
        #Add the weapon type, the model name, and the common name to the tree table
        
        a = 0
        for weapon_type, common_names in weaponss.items():
            for weapon in common_names:
                print(a)
                if(a>5):
                    weapon_tree.addTopLevelItem(QTreeWidgetItem([weapon_type, weapon, common_names]))
                a = a + 1
        

        layout.addWidget(weapon_tree)
        
        
        #Get Model From Tree Table
        def getModel(item):
            global selected_model, weapon_class, weapon_IN
            selected_model = weapon_tree.currentItem()
            global weapon_class
            weapon_class = selected_model.text(0)
            global weapon_IN
            weapon_IN = selected_model.text(1)
            print(weapon_class, weapon_IN)
        weapon_tree.currentItemChanged.connect(getModel)
        

        
        #Create a label
        model_list = QLabel("Weapon Type: ")
        model_list.setStyleSheet("font: bold;")
        layout.addWidget(model_list)



        #Create new list of weapons
        global weapons
        weapons = QListWidget()
        weapons.addItem("Rifle")
        weapons.addItem("Shotgun")
        weapons.addItem("Sniper")
        weapons.addItem("Pistol")
        layout.addWidget(weapons)


        #Create label for ammo list
        global ammo_list
        ammo_list = QLabel("Ammo List: ")
        ammo_list.setStyleSheet("font: bold;")
        layout.addWidget(ammo_list)

        #Create new list of ammo types
        global ammo_types
        ammo_types = QListWidget()
        ammo_types.addItem("Heavy Ammo")
        ammo_types.addItem("Light Ammo")
        ammo_types.addItem("Energy Ammo")
        ammo_types.addItem("Shotgun Ammo")
        layout.addWidget(ammo_types)

        #Create label for weapon damage
        weapon_damage = QLabel("Weapon Damage: ")
        weapon_damage.setStyleSheet("font: bold;")
        layout.addWidget(weapon_damage)

        #Create weapon damage near input
        global weapon_near
        weapon_near = QLineEdit()
        weapon_near.setPlaceholderText("Weapon Damage Near: ")
        layout.addWidget(weapon_near)

        #Create weapon damage far input
        global weapon_far
        weapon_far = QLineEdit()
        weapon_far.setPlaceholderText("Weapon Damage Far: ")
        layout.addWidget(weapon_far)

        #Create Weapon List Button
        list_weapon = QPushButton("Generate Weapon")
        list_weapon.clicked.connect(self.generate_weapon)
        layout.addWidget(list_weapon)

        
        #Add Widgets to layout
        self.setLayout(layout)

        

    #Generate the weapon using user input
    def generate_weapon(self):
        global ammo_types
        
        weapon_rifle = os.path.join(os.path.dirname(__file__), "weapon_types/mp_weapon_types.txt")
        print(selected_model)
        
        #Check if user input is valid
        if weapon_name.text() == "" or weapon_description.text() == "" or weapon_near.text() == "" or weapon_far.text() == "" or ammo_types.count() == 0:
            QMessageBox.warning(self, "Error", "Please fill out all fields")
            return
        #elif user input is not an integer
        elif not weapon_near.text().isdigit() or not weapon_far.text().isdigit():
            QMessageBox.warning(self, "Error", "Please enter valid numbers")
            return
        
        #Clone weapon_rifle to game_folder
        print(weapon_rifle)
        

        #Give user success popup
        QMessageBox.information(self, "Success", "Weapon created with info: \n" + "Name: " + weapon_name.text() + "\n" + "Desc: "
                                + weapon_description.text() + "\n" + "Near Damage: " + weapon_near.text() + "\n" + "Far Damage: " 
                                + weapon_far.text() + "Model: " + selected_model + "\nGenerated at: " + game_folder)
            


    
    

#Create new window
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("R5 Reloaded | Weapon Maker")
        self.setGeometry(600, 350, 650, 300)
        
        #Create settings menu
        settings_menu = QMenu("Settings", self)
        self.menuBar().addMenu(settings_menu)
        
        
        game_folder = settings_menu.addAction("Choose Game Folder")
    
        
        #If help action is pressed, open the help window
        help_action = settings_menu.addAction("Help")
        

        #If exit action is pressed, close the window
        exit_action = settings_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        tab_widget = QTabWidget(self)
        tab1 = Tab1()
        tab_widget.addTab(tab1, "Weapon Builder")
        self.setCentralWidget(tab_widget)

        #Create a function to open a link when help action is pressed
        def openLink():
            webbrowser.open("https://github.com/BrickOnAWall/R5-Reloaded-Weapon-Maker")
            
        #Create a function to select a game folder when game folder is pressed
        def folderOpener():
            folder = QFileDialog.getExistingDirectory(self, "Select Game Folder")
            
            #Create a file that saves the folder path 
            #Check if folder already exists
            if os.path.exists("game_folder.txt"):
                with open("game_folder.txt", "r") as f:
                    f.write(folder)

            with open("game_folder.txt", "w") as f:
                f.write(folder)
                
        

        help_action.triggered.connect(openLink)
        game_folder.triggered.connect(folderOpener)
        

#Start window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    if os.path.exists("game_folder.txt"):
                with open("game_folder.txt", "r") as f:
                    game_folder = os.pat
                    print(game_folder)
    else:
        game_folder = os.path.join(os.path.dirname(__file__), "game_folder")
                    
    window.show()
    sys.exit(app.exec_())

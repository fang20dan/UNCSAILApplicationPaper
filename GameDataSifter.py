import openpyxl
import GameClass

data = openpyxl.load_workbook("Miles_Mikolas_AdvancedPitchingStats.xlsx")
sh = data.active

date = "10/3/22"
games = []
game1 = GameClass.game([],[],[])

for i in range(2, sh.max_row+1):
    if sh.cell(row = i, col = 2).value == date:
        game1.addPitches(sh.cell(row = i, col = 1).value)
        game1.addEvents(sh.cell(row = i, col = 10).value)
        if sh.cell(row = i, col = 10).value == "hit_into_play":
            game1.addOutcomes(sh.cell(row = i, col = 9).value)
        else:
            game1.addOutcomes(sh.cell(row = i, col = 9).value)
    else:
        date = sh.cell(row = i, col = 2).value
        
import Parser
import save.spreadSheet as sS

if __name__ == '__main__':
    sS.save_to_xlsx(Parser.parse(), "test.xlsx")

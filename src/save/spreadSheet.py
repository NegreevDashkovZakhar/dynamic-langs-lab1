from Parser.model.property import Property
import xlsxwriter


def save_to_xlsx(properties: "list[Property]", file_name):
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    i = 1
    for property_ in properties:
        worksheet.write('A{}'.format(i), property_.rooms_count)
        worksheet.write('B{}'.format(i), property_.address)
        worksheet.write('C{}'.format(i), property_.area)
        worksheet.write('D{}'.format(i), property_.description)
        worksheet.write('E{}'.format(i), property_.price)
        i+=1

    workbook.close()

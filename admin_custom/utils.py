from django.http.response import HttpResponse
import xlwt


class FileExcel:
	def __init__(self, name_file, shet_name):
		self.shet_name = shet_name
		self.name_file = name_file
		self.response = HttpResponse(content_type='application/ms-excel')
		self.wb = xlwt.Workbook(encoding='utf-8')
		self.ws = self.wb.add_sheet(self.shet_name)
		self.font_style = xlwt.XFStyle()
		self.font_style.font.bold = True
		self.row_num = 0

	def write_file_medical(self, columns, data):
		self.response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(
			self.name_file)
		for col_num in range(len(columns)):
			self.ws.write(self.row_num, col_num, columns[col_num], self.font_style)

		font_style_body = xlwt.XFStyle()
		for my_row in data:
			self.row_num = self.row_num + 1

			if my_row.parentDiabetes == True:
				my_row.parentDiabetes = 'Si'
			else:
				my_row.parentDiabetes == 'NO'

			self.ws.write(self.row_num, 0, my_row.name_full, font_style_body)
			self.ws.write(self.row_num, 1, my_row.date_of_birth, font_style_body)
			self.ws.write(self.row_num, 2, my_row.sex, font_style_body)
			self.ws.write(self.row_num, 3, my_row.marital_status, font_style_body)
			self.ws.write(self.row_num, 4, my_row.nationality, font_style_body)
			self.ws.write(self.row_num, 5, my_row.profession, font_style_body)
			self.ws.write(self.row_num, 6, my_row.postal_code, font_style_body)
			self.ws.write(self.row_num, 7, my_row.address, font_style_body)
			self.ws.write(self.row_num, 8, my_row.email, font_style_body)
			self.ws.write(self.row_num, 9, my_row.num_phone, font_style_body)
			self.ws.write(self.row_num, 10, my_row.weight, font_style_body)
			self.ws.write(self.row_num, 11, my_row.height, font_style_body)
			self.ws.write(self.row_num, 12, my_row.parentDiabetes, font_style_body)
			self.ws.write(self.row_num, 13, my_row.sick, font_style_body)
			self.ws.write(self.row_num, 14, my_row.comments, font_style_body)

		self.wb.save(self.response)

	def write_file_life(self, columns, data):
		self.response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(
			self.name_file)
		for col_num in range(len(columns)):
			self.ws.write(self.row_num, col_num, columns[col_num], self.font_style)

		font_style_body = xlwt.XFStyle()
		for my_row in data:

			self.row_num = self.row_num + 1

			if my_row.smoker == True:
				my_row.smoker = 'Si'
			else:
				my_row.smoker == 'No'

			if my_row.sick == True:
				my_row.sick = 'Si'
			else:
				my_row.sick == 'No'

				self.ws.write(self.row_num, 0, my_row.name_full, font_style_body)
				self.ws.write(self.row_num, 1, my_row.date_of_birth, font_style_body)
				self.ws.write(self.row_num, 2, my_row.sex, font_style_body)
				self.ws.write(self.row_num, 3, my_row.marital_status, font_style_body)
				self.ws.write(self.row_num, 4, my_row.nationality, font_style_body)
				self.ws.write(self.row_num, 5, my_row.profession, font_style_body)
				self.ws.write(self.row_num, 6, my_row.postal_code, font_style_body)
				self.ws.write(self.row_num, 7, my_row.address, font_style_body)
				self.ws.write(self.row_num, 8, my_row.email, font_style_body)
				self.ws.write(self.row_num, 9, my_row.num_phone, font_style_body)
				self.ws.write(self.row_num, 10, my_row.weight, font_style_body)
				self.ws.write(self.row_num, 11, my_row.height, font_style_body)
				self.ws.write(self.row_num, 12, my_row.smoker, font_style_body)
				self.ws.write(self.row_num, 13, my_row.sick, font_style_body)
				self.ws.write(self.row_num, 14, my_row.type_insurance, font_style_body)
				self.ws.write(self.row_num, 15, my_row.mount_year, font_style_body)
				self.ws.write(self.row_num, 16, my_row.comments, font_style_body)

		self.wb.save(self.response)


	def write_file_car(self, columns, data):
		self.response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(
			self.name_file)
		for col_num in range(len(columns)):
			self.ws.write(self.row_num, col_num, columns[col_num], self.font_style)

		font_style_body = xlwt.XFStyle()
		for my_row in data:

			self.row_num = self.row_num + 1

			self.ws.write(self.row_num, 0, my_row.vehicle_type, font_style_body)
			self.ws.write(self.row_num, 1, my_row.model, font_style_body)
			self.ws.write(self.row_num, 2, my_row.description_vehicle, font_style_body)
			self.ws.write(self.row_num, 3, my_row.coverage_type, font_style_body)
			self.ws.write(self.row_num, 4, my_row.coverage_optional, font_style_body)
			self.ws.write(self.row_num, 5, my_row.name_full, font_style_body)
			self.ws.write(self.row_num, 6, my_row.date_of_birth, font_style_body)
			self.ws.write(self.row_num, 7, my_row.sex, font_style_body)
			self.ws.write(self.row_num, 8, my_row.postal_code, font_style_body)
			self.ws.write(self.row_num, 9, my_row.email, font_style_body)
			self.ws.write(self.row_num, 10, my_row.num_phone, font_style_body)
			self.ws.write(self.row_num, 11, my_row.comments, font_style_body)

		self.wb.save(self.response)


	def write_file_house(self, columns, data):
		self.response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(self.name_file)
		for col_num in range(len(columns)):
			self.ws.write(self.row_num, col_num, columns[col_num], self.font_style)

		font_style_body = xlwt.XFStyle()
		for my_row in data:
			
			self.row_num = self.row_num + 1
			
			if my_row.house_in_river == True:
				my_row.house_in_river = 'Si'
			else:
				my_row.house_in_river = 'No'


			self.ws.write(self.row_num, 0, my_row.street, font_style_body)
			self.ws.write(self.row_num, 1, my_row.number, font_style_body)
			self.ws.write(self.row_num, 2, my_row.suburb, font_style_body)
			self.ws.write(self.row_num, 3, my_row.postal_code, font_style_body)
			self.ws.write(self.row_num, 4, my_row.city, font_style_body)
			self.ws.write(self.row_num, 5, my_row.state, font_style_body)
			self.ws.write(self.row_num, 6, my_row.housing_type, font_style_body)
			self.ws.write(self.row_num, 7, my_row.year_house, font_style_body)
			self.ws.write(self.row_num, 8, my_row.coverage_type, font_style_body)
			self.ws.write(self.row_num, 9, my_row.house_in_river, font_style_body)
			self.ws.write(self.row_num, 10, my_row.security_measures, font_style_body)
			self.ws.write(self.row_num, 11, my_row.name_full, font_style_body)
			self.ws.write(self.row_num, 12, my_row.contract_type, font_style_body)
			self.ws.write(self.row_num, 13, my_row.email, font_style_body)
			self.ws.write(self.row_num, 14, my_row.num_phone, font_style_body)
			self.ws.write(self.row_num, 15, my_row.comments, font_style_body)
						

		
		
		self.wb.save(self.response)	

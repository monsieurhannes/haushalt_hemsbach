i = 1
export_file = "haushalt" + str(i) + ".csv"
convert_into("haushalt.pdf", "export_file", output_format="csv", pages="1-10")
for i in range(1,6):
  export_file = "haushalt" + str(i) + ".csv"
  page_range = str(i * 10 + 1) + "-" + str(i * 10 + 10)
  convert_into("haushalt.pdf", export_file, output_format="csv", pages=page_range)

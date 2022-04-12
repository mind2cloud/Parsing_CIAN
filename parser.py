from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv

#CIAN got:  1379
class cian_flats_parser():
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        # self.go_to_flat_page()
        self.flat_data_grabber()

    def go_to_flat_page(self):
        page_begin = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p='
        page_end = '&region=1&room1=1&room2=1'
        with open('hrefs_3.txt', 'w') as f:
            for page in range(70, 90):
                print("page #", page)
                self.driver.get(page_begin + str(page) + page_end)
                hrefs = self.driver.find_elements_by_class_name("_93444fe79c--link--39cNw")
                for href in hrefs:
                    href_link = href.get_attribute('href')
                    print(href_link)
                    f.write(str(href_link) + '\n')
        f.close()

                #self.driver.get(href_link)
                #self.flat_data_grabber(href_link)
                # break
            # self.driver.close()

    def flat_data_grabber(self):
        with open('hrefs.txt', 'r') as f:
            hrefs = [row.strip() for row in f]
        data = {}
        count = 0
        csv_file = "cian_flats_2000_2.csv"

        with open(csv_file, 'w') as csvfile:
            for href in hrefs:
                self.driver.get(href)

                address = " "
                metro_stations = " "
                price = " "
                price_per_meter = " "
                developer = " "
                additional_flat_info = " "
                total_info = " "
                living_square = " "
                kitchen_square = " "
                bti_house_data = " "

                try:
                    address = self.driver.find_element_by_class_name('a10a3f92e9--address--140Ec').text
                    #print(address)
                    data['address'] = address
                    #print(data['address'])
                except Exception:
                    data['address'] = "N_A"

                try:
                    metro_stations = self.driver.find_element_by_class_name('a10a3f92e9--undergrounds--2pop3').text
                    data['metro_stations'] = metro_stations
                    #print(data['metro_stations'])
                except Exception:
                    data['metro_stations'] = "N_A"

                try:
                    total_info = self.driver.find_element_by_class_name('a10a3f92e9--info-block--3cWJy').text
                    data['total_info'] = total_info
                    #print(data['total_info'])
                except Exception:
                    data['total_info'] = "N_A"

                try:
                    price = self.driver.find_element_by_class_name('a10a3f92e9--price_value--1iPpd').text
                    data['price'] = price
                    #print(data['price'])
                except Exception:
                    data['price'] = "N_A"

                try:
                    price_per_meter = self.driver.find_element_by_xpath('/html/body/div[6]/main/div[3]/div/div[1]/div[1]/div[1]/div/div[1]/div').text
                    data['price_per_meter'] = price_per_meter
                    #print(data['price_per_meter'])
                except Exception:
                    data['price_per_meter'] = "N_A"

                try:
                    # name_developer = self.driver.find_element_by_xpath('a10a3f92e9--honest-container--289-k').text
                    # developer = self.driver.find_element_by_class_name('a10a3f92e9--title--2gUWg').text
                    # print(name_developer)
                    # if name_developer == 'Застройщик':
                    #     data['developer'] = developer
                    # else:
                    #     data['developer'] = "N_A"
                    #print(data['developer'])
                    developer = self.driver.find_element_by_class_name('a10a3f92e9--title--2gUWg').text
                    data['developer'] = developer
                except Exception:
                    data['developer'] = "N_A"

                try:
                    additional_flat_info = self.driver.find_element_by_class_name('a10a3f92e9--container--1MHfF').text
                    data['additional_flat_info'] = additional_flat_info
                    #print(data['additional_flat_info'])
                except Exception:
                    data['additional_flat_info'] = "N_A"

                try:
                    bti_house_data = self.driver.find_element_by_class_name('a10a3f92e9--container--3dDSQ').text
                    data['bti_house_data'] = bti_house_data
                    #print(data['bti_house_data'])
                except Exception:
                    data['bti_house_data'] = "N_A"

                #print(data)
                print('CIAN got: ', count+1)

                writer = csv.DictWriter(csvfile, fieldnames=data.keys())
                if (count == 0):
                    writer.writeheader()
                writer.writerow(data)
                count += 1
                if count == 2001:
                    break

        # return data

class domofond_flats_parser():
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        # self.go_to_flat_page()
        self.flat_data_grabber()

    def go_to_flat_page(self):
        page_w_o_number = 'https://www.domofond.ru/prodazha-kvartiry-moskva-c3584?Page='
        with open('hrefs_domofond_start_with_2359.txt', 'w') as f:
            for page in range(2359, 2401):
                print("page #", page)
                self.driver.get(page_w_o_number + str(page))
                hrefs = self.driver.find_elements_by_class_name("long-item-card__item___ubItG")
                for href in hrefs:
                    href_link = href.get_attribute('href')
                    print(href_link)
                    f.write(str(href_link) + '\n')
        f.close()

    def flat_data_grabber(self):
        with open('hrefs_domofond_5.txt', 'r') as f:
            hrefs = [row.strip() for row in f]
        data = {}
        count = 0
        csv_file = "flats_domofond_2000_2.csv"

        with open(csv_file, 'w') as csvfile:
            for href in hrefs:
                self.driver.get(href)

                address = " "
                metro_station = " "
                type = " "
                type_object = " "
                price = " "
                price_per_meter = " "
                n_rooms = " "
                floor = " "
                square_total = " "
                square_living = " "
                square_kitchen = " "
                wall_type = " "
                series = " "
                ad_number = " "
                year_built = " "
                year_start_operation = " "
                floor_max = " "
                floor_min = " "
                entrances_number = " "
                overlaps = " "      # перекрытия
                garbage_chute = " " # мусоропровод
                heating = " "       # отопление
                gas_stove = " "     # газовая плита

                try:
                    address = self.driver.find_element_by_class_name('information__address___1ZM6d').text
                    # print(address)
                    data['address'] = address
                    # print(data['address'])
                except Exception:
                    data['address'] = "N_A"

                try:
                    metro_station = self.driver.find_element_by_class_name('information__metro___2zFqN').text
                    data['metro_station'] = metro_station
                    # print(data['metro_station'])
                except Exception:
                    data['metro_station'] = "N_A"

                try:
                    name_type = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[1]/span[1]').text
                    type = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[1]/span[2]').text
                    # print("name_type: ", name_type)
                    if name_type == "Тип:":
                        # print("type YES")
                        data['type'] = type
                    else:
                        data['type'] = "N_A"
                    # print(data['type'])
                except Exception:
                    data['type'] = "N_A"

                try:
                    name_type_object = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[2]/span[1]').text
                    type_object = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[2]/span[2]').text
                    # print("name_type_object: ", name_type_object)
                    if name_type_object == "Тип объекта:":
                        # print("name_type_object YES")
                        data['type_object'] = type_object
                    else:
                        data['type_object'] = "N_A"
                    # print(data['type_object'])
                except Exception:
                    data['type_object'] = "N_A"

                try:
                    price = self.driver.find_element_by_class_name('information__price___2Lpc0').text
                    data['price'] = price
                    # print(data['price'])
                except Exception:
                    data['price'] = "N_A"

                try:
                    name_price_per_meter = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[9]/span[1]').text
                    price_per_meter = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[9]/span[2]').text
                    # print("name_price_per_meter: ", name_price_per_meter)
                    if name_price_per_meter == "Цена за м²:":
                        # print("name_price_per_meter YES")
                        data['price_per_meter'] = price_per_meter
                    else:
                        data['price_per_meter'] = "N_A"
                    # print(data['price_per_meter'])
                except Exception:
                    data['price_per_meter'] = "N_A"

                try:
                    name_n_rooms = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[3]/span[1]').text
                    n_rooms = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[3]/span[2]').text
                    # print("name_n_rooms: ", name_n_rooms)
                    if name_n_rooms == "Комнаты:":
                        # print("name_n_rooms YES")
                        data['n_rooms'] = n_rooms
                    else:
                        data['n_rooms'] = "N_A"
                    # print(data['n_rooms'])
                except Exception:
                    data['n_rooms'] = "N_A"

                try:
                    name_floor = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[4]/span[1]').text
                    floor = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[4]/span[2]').text
                    # print("name_floor: ", name_floor)
                    if name_floor == "Этаж:":
                        # print("name_floor YES")
                        data['floor'] = floor
                    else:
                        data['floor'] = "N_A"
                    # print(data['floor'])
                except Exception:
                    data['floor'] = "N_A"

                try:
                    name_square_total = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[5]/span[1]').text
                    square_total = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[5]/span[2]').text
                    # print("name_square_total: ", name_square_total)
                    if name_square_total == "Площадь:":
                        # print("name_square_total YES")
                        data['square_total'] = square_total
                    else:
                        data['square_total'] = "N_A"
                    # print(data['square_total'])
                except Exception:
                    data['square_total'] = "N_A"

                try:
                    name_square_living = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[7]/span[1]').text
                    square_living = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[7]/span[2]').text
                    # print("name_square_living: ", name_square_living)
                    if name_square_living == "Жилая площадь (м²):":
                        # print("name_square_living YES")
                        data['square_living'] = square_living
                    else:
                        data['square_living'] = "N_A"
                    # print(data['square_living'])
                except Exception:
                    data['square_living'] = "N_A"

                try:
                    name_square_kitchen = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[6]/span[1]').text
                    square_kitchen = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[6]/span[2]').text
                    # print("name_square_kitchen: ", name_square_kitchen)
                    if name_square_kitchen == "Площадь кухни (м²):":
                        # print("name_square_kitchen YES")
                        data['square_kitchen'] = square_kitchen
                    else:
                        data['square_kitchen'] = "N_A"
                    # print(data['square_kitchen'])
                except Exception:
                    data['square_kitchen'] = "N_A"

                try:
                    name_wall_type = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[10]/span[1]').text
                    wall_type = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[10]/span[2]').text
                    # print("name_wall_type: ", name_wall_type)
                    if name_wall_type == "Материал здания:":
                        # print("name_wall_type YES")
                        data['wall_type'] = wall_type
                    else:
                        data['wall_type'] = "N_A"
                    # print(data['wall_type'])
                except Exception:
                    data['wall_type'] = "N_A"

                try:
                    name_series = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[3]/span[1]').text
                    series = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[3]/span[2]').text
                    # print("name_series: ", name_series)
                    if name_series == "Серия:":
                        # print("name_series YES")
                        data['series'] = series
                    else:
                        data['series'] = "N_A"
                    # print(data['series'])
                except Exception:
                    data['series'] = "N_A"

                try:
                    name_ad_number = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[13]/span[1]').text
                    ad_number = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[7]/div/div[13]/span[2]').text
                    # print("name_ad_number: ", name_ad_number)
                    if name_ad_number == "Номер в каталоге:":
                        # print("name_ad_number YES")
                        data['ad_number'] = ad_number
                    else:
                        data['ad_number'] = "N_A"
                    # print(data['ad_number'])
                except Exception:
                    data['ad_number'] = "N_A"

                try:
                    name_year_built = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[1]/span[1]').text
                    year_built = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[1]/span[2]').text
                    # print("name_year_built: ", name_year_built)
                    if name_year_built == "Год постройки:":
                        # print("name_year_built YES")
                        data['year_built'] = year_built
                    else:
                        data['year_built'] = "N_A"
                    # print(data['year_built'])
                except Exception:
                    data['year_built'] = "N_A"

                try:
                    name_year_start_operation = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[2]/span[1]').text
                    year_start_operation = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[2]/span[2]').text
                    # print("name_year_start_operation: ", name_year_start_operation)
                    if name_year_start_operation == "Год ввода в эксплуатацию:":
                        # print("name_year_start_operation YES")
                        data['year_start_operation'] = year_start_operation
                    else:
                        data['year_start_operation'] = "N_A"
                    # print(data['year_start_operation'])
                except Exception:
                    data['year_start_operation'] = "N_A"

                try:
                    name_floor_max = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[5]/span[1]').text
                    floor_max = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[5]/span[2]').text
                    # print("name_floor_max: ", name_floor_max)
                    if name_floor_max == "Макс. этажность:":
                        # print("name_floor_max YES")
                        data['floor_max'] = floor_max
                    else:
                        data['floor_max'] = "N_A"
                    # print(data['floor_max'])
                except Exception:
                    data['floor_max'] = "N_A"

                try:
                    name_floor_min = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[6]/span[1]').text
                    floor_min = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[6]/span[2]').text
                    if name_floor_min == "Мин. этажность:":
                        # print("name_floor_min YES")
                        data['floor_min'] = floor_min
                    else:
                        data['floor_min'] = "N_A"
                    # print(data['floor_min'])
                except Exception:
                    data['floor_min'] = "N_A"

                try:
                    name_entrances_number = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[7]/span[1]').text
                    entrances_number = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[7]/span[2]').text
                    # print("name_entrances_number: ", name_entrances_number)
                    if name_entrances_number == "Кол-во подьездов:":
                        # print("name_entrances_number YES")
                        data['entrances_number'] = entrances_number
                    else:
                        data['entrances_number'] = "N_A"
                    # print(data['entrances_number'])
                except Exception:
                    data['entrances_number'] = "N_A"

                try:
                    name_overlaps = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[8]/span[1]').text
                    overlaps = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[8]/span[2]').text
                    # print("name_overlaps: ", name_overlaps)
                    if name_overlaps == "Перекрытия:":
                        # print("name_overlaps YES")
                        data['overlaps'] = overlaps
                    else:
                        data['overlaps'] = "N_A"
                    # print(data['overlaps'])
                except Exception:
                    data['overlaps'] = "N_A"

                try:
                    name_garbage_chute = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[10]/span[1]').text
                    garbage_chute = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[10]/span[2]').text
                    # print("name_garbage_chute: ", name_garbage_chute)
                    if name_garbage_chute == "Мусоропровод:":
                        # print("name_garbage_chute YES")
                        data['garbage_chute'] = garbage_chute
                    else:
                        data['garbage_chute'] = "N_A"
                    # print(data['garbage_chute'])
                except Exception:
                    data['garbage_chute'] = "N_A"

                try:
                    name_heating = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[11]/span[1]').text
                    heating = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[11]/span[2]').text
                    # print("name_heating: ", name_heating)
                    if name_heating == "Отопление:":
                        # print("name_heating YES")
                        data['heating'] = heating
                    else:
                        data['heating'] = "N_A"
                    # print(data['heating'])
                except Exception:
                    data['heating'] = "N_A"

                try:
                    name_gas_stove = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[12]/span[1]').text
                    gas_stove = self.driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[1]/div[8]/div/div[12]/span[2]').text
                    # print("name_gas_stove: ", name_gas_stove)
                    if name_gas_stove == "Газ.плита:":
                        # print("name_gas_stove YES")
                        data['gas_stove'] = gas_stove
                    else:
                        data['gas_stove'] = "N_A"
                    # print(data['gas_stove'])
                except Exception:
                    data['gas_stove'] = "N_A"

                # print(data)
                print('Domofond got: ', count + 1)

                writer = csv.DictWriter(csvfile, fieldnames=data.keys())
                if (count == 0):
                    writer.writeheader()
                writer.writerow(data)
                count += 1
                if count == 10001:
                    break

        # return data


def main():
    # driver = webdriver.Chrome('./chromedriver')
    cian_driver = webdriver.Chrome('./chromedriver')
    cian_parser = cian_flats_parser(cian_driver)
    cian_parser.parse()
    # domofond_driver = webdriver.Chrome('./chromedriver')
    # domofond_parser = domofond_flats_parser(domofond_driver)
    # domofond_parser.parse()


if __name__ == "__main__":
    main()
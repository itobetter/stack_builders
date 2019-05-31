import calendar
import datetime as dt
import re

class PlatePredictor():

    def __init__(self, plate, now):
        self.plate =  re.match('(\w{3})-(\d{3}$)', plate)
        self.validate_plate()
        # 'year/moneth/day hour:minutes:secund'
        self.now = dt.datetime.strptime(now, '%Y/%m/%d %H:%M:%S')
        self.first_segment = self.plate.group(1)
        self.first_letter = self.first_segment[0]
        self.secund_segment = self.plate.group(2)
        self.secund_letter = self.first_segment[1]
        self.last_letter = self.secund_segment[-1]


    def validate_plate(self):
        if not self.plate:
            raise


    def get_provincial(self):
        return {
            'A': 'Azuay',
            'B': 'Bolívar',
            'U': 'Cañar',
            'C': 'Carchi',
            'X': 'Cotopaxi',
            'H': 'Chimborazo',
            'O': 'El Oro',
            'E': 'Esmeraldas',
            'W': 'Galápagos',
            'g': 'Guayas',
            'I': 'Imbabura',
            'L': 'Loja',
            'R': 'Los Ríos',
            'M': 'Manabí',
            'V': 'Morona Santiago',
            'N': 'Napo',
            'S': 'Pastaza',
            'P': 'Pichincha',
            'K': 'Sucumbíos',
            'Q': 'Orellana',
            'T': 'Tungurahua',
            'Z': 'Zamora Chinchipe',
            'Y': 'Santa Elena'
        }.get(self.first_letter) or 'Unknown'


    def get_type(self):
        return {
            'A':'Commercial Vehicle',
            'Z': 'Commercial Vehicle',
            'E': 'Government Vehicle',
            'X': 'Official Use Vehicle',
            'S': 'Provincial Government Vehicle',
            'M':'Municipal Vehicles'
        }.get(self.secund_letter) or 'private vehicle'
        
        
    def get_can_road(self):
        xrange_days = [
            (1,2),(3,4),
            (5,6),(7,8),
            (9,0)
        ]
        weekday = calendar.weekday(self.now.year,self.now.month,self.now.day)
        return 'Yes' if 0 <= weekday <= 4 and self.last_letter not in xrange_days[weekday] else 'Dont'


    def get_info(self):
        return """Plate :{0} </br> Provincial: {1} </br> Type: {2} </br> Can road: {3} </br>""".format(
            "-".join(self.plate.groups()),
            self.get_provincial(),
            self.get_type(),
            self.get_can_road()
        )


if __name__ == "__main__":
    plate = input('Insert your plate')
    time = input('Insert datetime in format Year/month/day hour:minutes:secunds')
    PlatPred = PlatePredictor(plate,time)
    print(PlatPred.get_info())
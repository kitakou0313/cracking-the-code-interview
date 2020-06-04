import unittest


class Car():
    def __init__(self, typeName):
        self.__type = typeName

    def getVehicleType(self):
        return self.__type


class ParkSpace():
    def __init__(self, vehicleType, level):
        self.__vehicleType = vehicleType
        self.__parkedVehicle = None
        self.__level = level

    def getParkSpaceLevel(self):
        return self.__level

    def getParkableVehicleType(self):
        return self.__vehicleType

    def isParkable(self):
        return self.__parkedVehicle == None

    def getVehicle(self):
        return self.__parkedVehicle

    def parkCar(self, vehicle):
        self.__parkedVehicle = vehicle

    def unparkCar(self, vehicle):
        self.__parkedVehicle = None


class ParkingLot():
    def __init__(self, levelNum, largeNum, middleNum, smallNum):
        self.__largeSpace = [[ParkSpace("L", level) for i in range(
            largeNum)] for level in range(levelNum)]

        self.__middleSpace = [[ParkSpace("M", level) for i in range(
            middleNum)] for level in range(levelNum)]

        self.__smallSpace = [[ParkSpace("S", level) for i in range(
            smallNum)]for level in range(levelNum)]

        self.parkedCarList = {}

    def getLargeCar(self):
        return self.__largeSpace

    def getSmallCar(self):
        return self.__smallSpace

    def parkCar(self, car):
        if car.getVehicleType() == "L":
            for level in range(len(self.__largeSpace)):
                for space in self.__largeSpace[level]:
                    if car in self.parkedCarList:
                        continue
                    if space.isParkable():
                        space.parkCar(car)
                        self.parkedCarList[car] = [level, space]

        elif car.getVehicleType() == "M":
            for level in range(len(self.__middleSpace)):
                for space in self.__middleSpace[level]:
                    if car in self.parkedCarList:
                        continue
                    if space.isParkable():
                        space.parkCar(car)
                        self.parkedCarList[car] = [level, space]
        else:
            for level in range(len(self.__smallSpace)):
                for space in self.__smallSpace[level]:
                    if car in self.parkedCarList:
                        continue
                    if space.isParkable():
                        space.parkCar(car)
                        self.parkedCarList[car] = [level, space]

    def unparkCar(self, car):
        carInfo = self.parkedCarList[car]
        if car.getVehicleType() == "L":
            for space in self.__largeSpace[carInfo[0]]:
                if space == carInfo[1]:
                    space.unparkCar(car)
        elif car.getVehicleType() == "M":
            for space in self.__middleSpace[carInfo[0]]:
                if space == carInfo[1]:
                    space.unparkCar(car)
        else:
            for space in self.__smallSpace[carInfo[0]]:
                if space == carInfo[1]:
                    space.unparkCar(car)
        self.parkedCarList.pop(car)


class Test(unittest.TestCase):
    def test_parking_lot(self):
        lot = ParkingLot(2, 2, 2, 2)
        car1 = Car("S")
        car2 = Car("L")
        lot.parkCar(car1)
        lot.parkCar(car2)
        self.assertEqual(len(lot.parkedCarList), 2)
        self.assertEqual(lot.getSmallCar()[0][0].getVehicle(), car1)
        self.assertEqual(lot.getLargeCar()[0][0].getVehicle(), car2)

        lot.unparkCar(car1)
        self.assertEqual(len(lot.parkedCarList), 1)
        self.assertEqual(lot.getSmallCar()[0][0].getVehicle(), None)
        self.assertEqual(lot.getLargeCar()[0][0].getVehicle(), car2)


if __name__ == "__main__":
    unittest.main()

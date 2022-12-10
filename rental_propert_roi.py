class RoiCalc():
    def __init__(self, investment, rent, loss):
        self.investment = investment
        self.rent = rent
        self.loss = loss
        cashflow = rent * 12 - loss
        ROI = (cashflow/investment)*100
        print("The ROI for your investment property is " +
              str(ROI) + "%" + " annually")


investment = int(
    input("How much capital was used to secure this investment? "))
rent = int(input("How much money do your tentants pay in rent monthly? or if vacant want is the average rent in your area? "))
loss = int(input("What are your yearly expenses to maintain your rental? "))
RoiCalc(investment, rent, loss)

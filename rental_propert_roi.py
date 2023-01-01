class RoiCalc():
    def __init__(self, income, expenses, cashflow, investment, roi):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.investment = investment
        self.roi = roi

        print("The ROI for your investment property is " +
              str(roi) + "%" + " annually")


income = int(input(
    "How much money do your tentants pay in rent monthly? or if vacant what is the average rent in your area? "))*12
expenses = int(
    input("What are your yearly expenses to maintain your rental? "))
investment = int(
    input("How much capital was used to secure this investment? "))
cashflow = income - expenses
roi = (cashflow/investment)*100

RoiCalc(income, expenses, cashflow, investment, roi)

import math

class FinancialModel:
    def __init__(self, company_name):
        self.company_name = company_name
        self.revenue = 0
        self.ebitda = 0
        self.net_income = 0
        self.free_cash_flow = 0
        self.debt = 0
        self.cash = 0
        self.shares_outstanding = 0
        self.stock_price = 0

    def set_financials(self, revenue, ebitda, net_income, fcf, debt, cash, shares, price):
        self.revenue = revenue
        self.ebitda = ebitda
        self.net_income = net_income
        self.free_cash_flow = fcf
        self.debt = debt
        self.cash = cash
        self.shares_outstanding = shares
        self.stock_price = price

    def calculate_ratios(self):
        market_cap = self.stock_price * self.shares_outstanding
        enterprise_value = market_cap + self.debt - self.cash

        pe = self.stock_price / (self.net_income / self.shares_outstanding) if self.net_income > 0 else 0
        pb = self.stock_price / ((self.revenue * 0.2) / self.shares_outstanding)
        ev_ebitda = enterprise_value / self.ebitda if self.ebitda > 0 else 0

        return {
            "Market Cap": market_cap,
            "Enterprise Value": enterprise_value,
            "P/E Ratio": pe,
            "P/B Ratio": pb,
            "EV/EBITDA": ev_ebitda
        }

    def dcf_valuation(self, growth_rate=0.05, discount_rate=0.10, years=5):
        fcf = self.free_cash_flow
        terminal_growth = 0.03
        present_value = 0

        for i in range(1, years + 1):
            fcf_year = fcf * (1 + growth_rate) ** i
            pv = fcf_year / (1 + discount_rate) ** i
            present_value += pv

        terminal_value = fcf * (1 + terminal_growth) / (discount_rate - terminal_growth)
        pv_terminal = terminal_value / (1 + discount_rate) ** years

        total_value = present_value + pv_terminal
        intrinsic_value_per_share = total_value / self.shares_outstanding

        return {
            "Present Value of FCF": present_value,
            "Present Value of Terminal Value": pv_terminal,
            "Total Enterprise Value": total_value,
            "Intrinsic Value Per Share": intrinsic_value_per_share
        }

    def compare_competitors(self, competitors):
        print("\n" + "-" * 60)
        print("COMPETITOR COMPARISON".center(60))
        print("-" * 60)

        my_ratios = self.calculate_ratios()

        print(f"\n{self.company_name}:")
        print(f"  P/E: {my_ratios['P/E Ratio']:.2f}")
        print(f"  P/B: {my_ratios['P/B Ratio']:.2f}")
        print(f"  EV/EBITDA: {my_ratios['EV/EBITDA']:.2f}")

        for name, data in competitors.items():
            pe = data["price"] / (data["earnings"] / data["shares"])
            pb = data["price"] / (data["book_value"] / data["shares"])
            ev_ebitda = (data["market_cap"] + data["debt"] - data["cash"]) / data["ebitda"]

            print(f"\n{name}:")
            print(f"  P/E: {pe:.2f}")
            print(f"  P/B: {pb:.2f}")
            print(f"  EV/EBITDA: {ev_ebitda:.2f}")

    def recommendation(self, intrinsic_value):
        print("\n" + "=" * 60)
        print("   INVESTMENT RECOMMENDATION")
        print("=" * 60)

        print(f"Current Stock Price: ${self.stock_price:.2f}")
        print(f"Intrinsic Value: ${intrinsic_value:.2f}")

        if intrinsic_value > self.stock_price * 1.2:
            print("\n✅ BUY: Stock is undervalued.")
            print(f"   Margin of Safety: {((intrinsic_value - self.stock_price) / self.stock_price * 100):.1f}%")
        elif intrinsic_value < self.stock_price * 0.8:
            print("\n❌ SELL: Stock is overvalued.")
            print(f"   Premium: {((self.stock_price - intrinsic_value) / intrinsic_value * 100):.1f}%")
        else:
            print("\n⚖️ HOLD: Stock is fairly valued.")

def main():
    print("\n" + "=" * 60)
    print("   FUNDAMENTAL VALUATION & FINANCIAL MODELING")
    print("=" * 60)

    company = FinancialModel("TechCorp Inc.")
    company.set_financials(
        revenue=5000000000,
        ebitda=1200000000,
        net_income=800000000,
        fcf=700000000,
        debt=2000000000,
        cash=500000000,
        shares=100000000,
        price=120
    )

    print(f"\n[1] Financial Data for {company.company_name}:")
    print("-" * 40)
    print(f"Revenue: ${company.revenue:,.0f}")
    print(f"EBITDA: ${company.ebitda:,.0f}")
    print(f"Net Income: ${company.net_income:,.0f}")
    print(f"Free Cash Flow: ${company.free_cash_flow:,.0f}")
    print(f"Debt: ${company.debt:,.0f}")
    print(f"Cash: ${company.cash:,.0f}")
    print(f"Shares Outstanding: {company.shares_outstanding:,.0f}")
    print(f"Stock Price: ${company.stock_price:.2f}")

    print("\n[2] Valuation Ratios:")
    print("-" * 40)
    ratios = company.calculate_ratios()
    for key, value in ratios.items():
        print(f"{key}: {value:.2f}")

    print("\n[3] Discounted Cash Flow (DCF) Analysis:")
    print("-" * 40)
    dcf = company.dcf_valuation(growth_rate=0.05, discount_rate=0.10)
    for key, value in dcf.items():
        print(f"{key}: ${value:,.2f}")

    print("\n[4] Competitor Comparison:")
    competitors = {
        "CompCorp": {"price": 90, "earnings": 500000000, "shares": 80000000, "book_value": 600000000, "market_cap": 7200000000, "debt": 1000000000, "cash": 300000000, "ebitda": 700000000},
        "ValueCorp": {"price": 150, "earnings": 300000000, "shares": 50000000, "book_value": 400000000, "market_cap": 7500000000, "debt": 1500000000, "cash": 400000000, "ebitda": 500000000}
    }
    company.compare_competitors(competitors)

    print("\n[5] Intrinsic Value Recommendation:")
    company.recommendation(dcf["Intrinsic Value Per Share"])

    print("\n" + "=" * 60)
    print("   VALUATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()
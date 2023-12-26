module SavingsAccount
  def self.interest_rate(balance)
    if balance < 0
      3.213
    elsif balance >= 0 && balance < 1000
      0.5
    elsif balance >= 1000 && balance < 5000
      1.621
    else
      2.475
    end
  end

  def self.annual_balance_update(balance)
    annual_change = SavingsAccount.interest_rate(balance) / 100 + 1
    if balance < 0
      balance *= -1
      balance *= annual_change
      return balance *= -1
    end
    balance *= annual_change
  end

  def self.years_before_desired_balance(current_balance, desired_balance)
    count = 0
    while current_balance < desired_balance
      current_balance = SavingsAccount.annual_balance_update(current_balance)
      count += 1
    end
    count
  end
end

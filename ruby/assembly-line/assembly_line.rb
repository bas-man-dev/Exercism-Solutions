class AssemblyLine
  PRODUCTION_RATE = 221

  def initialize(speed)
    @speed = speed
  end

  def production_rate_per_hour
    case @speed
    when 10 then return PRODUCTION_RATE * @speed * 0.77
    when 9 then return PRODUCTION_RATE * @speed * 0.8
    when 5, 6, 7, 8 then return PRODUCTION_RATE * @speed * 0.9
    when 1, 2, 3, 4 then return PRODUCTION_RATE * @speed
    else raise 'Not a valid speed'
    end
  end

  def working_items_per_minute
    (production_rate_per_hour / 60).floor()
  end
end

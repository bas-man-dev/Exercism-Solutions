class Attendee
  # I would make the height initialized then change it later so it's more obvious what's being done!
  attr_accessor :pass_id

  def initialize(height)
    @height = height
  end

  def issue_pass!(pass_id)
    @pass_id = pass_id
  end

  def revoke_pass!
    @pass_id = nil
  end

  # Do not edit above methods, add your own methods below.

  def has_pass?
    @pass_id ? true : false
  end

  def fits_ride?(ride_minimum_height)
    @height >= ride_minimum_height ? true : false
  end

  def allowed_to_ride?(ride_minimum_height)
    @pass_id && fits_ride?(ride_minimum_height) ? true : false
  end
end

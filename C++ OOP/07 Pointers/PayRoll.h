#pragma once
class PayRoll
{
private:
	double* hours;
	double* payRate;

public:
	PayRoll();
	~PayRoll();
	void setHours(double h);
	void setPayRate(double p);
	double getGrossPay() const;
};
Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tabby_cat="\tI'm tabbed in."
>>> persian_cat="I'm split\non a line"
>>> backlash_cat="I'm\a\\cat"
>>> fat_cat="""
hi
\t*cat food
\t*fishies
\t*catnip\nt* remember katniss :)"""
>>> print tabby_cat
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(tabby_cat)?
>>> print(tabby_cat)
	I'm tabbed in.
>>> print(persian_cat)
I'm split
on a line
>>> print(backlash_cat)
I'm\cat
>>> print(fat_cat)

hi
	*cat food
	*fishies
	*catnip
t* remember katniss :)
>>> fat_cat="""
hi
\t*goodmorning
\t*catnip
\n\t*no its katniss"""
>>> print(fat_cat)

hi
	*goodmorning
	*catnip

	*no its katniss
>>> 
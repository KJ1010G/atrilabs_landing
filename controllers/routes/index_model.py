from typing import Union, Any
from atri_react import Flex
from atri_react import Image
from atri_react import TextBox
from atri_react import Anchor
from atri_react import Video


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.container = state["container"] if "container" in state else None
		self.hero = state["hero"] if "hero" in state else None
		self.navbar = state["navbar"] if "navbar" in state else None
		self.main = state["main"] if "main" in state else None
		self.max_width = state["max_width"] if "max_width" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.row_1_hero = state["row_1_hero"] if "row_1_hero" in state else None
		self.open_source = state["open_source"] if "open_source" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.leave_a_star = state["leave_a_star"] if "leave_a_star" in state else None
		self.python_web_framework = state["python_web_framework"] if "python_web_framework" in state else None
		self.sub_title = state["sub_title"] if "sub_title" in state else None
		self.Video1 = state["Video1"] if "Video1" in state else None
		self.footer = state["footer"] if "footer" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.footer_logo = state["footer_logo"] if "footer_logo" in state else None
		self.social_icons = state["social_icons"] if "social_icons" in state else None
		self.anchor_github = state["anchor_github"] if "anchor_github" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.anchor_linkedin = state["anchor_linkedin"] if "anchor_linkedin" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.anchor_twitter = state["anchor_twitter"] if "anchor_twitter" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.footer_row_1 = state["footer_row_1"] if "footer_row_1" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def container(self):
		self._getter_access_tracker["container"] = {}
		return self._container
	@container.setter
	def container(self, new_state):
		self._setter_access_tracker["container"] = {}
		self._container = Flex(new_state)

	@property
	def hero(self):
		self._getter_access_tracker["hero"] = {}
		return self._hero
	@hero.setter
	def hero(self, new_state):
		self._setter_access_tracker["hero"] = {}
		self._hero = Flex(new_state)

	@property
	def navbar(self):
		self._getter_access_tracker["navbar"] = {}
		return self._navbar
	@navbar.setter
	def navbar(self, new_state):
		self._setter_access_tracker["navbar"] = {}
		self._navbar = Flex(new_state)

	@property
	def main(self):
		self._getter_access_tracker["main"] = {}
		return self._main
	@main.setter
	def main(self, new_state):
		self._setter_access_tracker["main"] = {}
		self._main = Flex(new_state)

	@property
	def max_width(self):
		self._getter_access_tracker["max_width"] = {}
		return self._max_width
	@max_width.setter
	def max_width(self, new_state):
		self._setter_access_tracker["max_width"] = {}
		self._max_width = Flex(new_state)

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def row_1_hero(self):
		self._getter_access_tracker["row_1_hero"] = {}
		return self._row_1_hero
	@row_1_hero.setter
	def row_1_hero(self, new_state):
		self._setter_access_tracker["row_1_hero"] = {}
		self._row_1_hero = Flex(new_state)

	@property
	def open_source(self):
		self._getter_access_tracker["open_source"] = {}
		return self._open_source
	@open_source.setter
	def open_source(self, new_state):
		self._setter_access_tracker["open_source"] = {}
		self._open_source = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def leave_a_star(self):
		self._getter_access_tracker["leave_a_star"] = {}
		return self._leave_a_star
	@leave_a_star.setter
	def leave_a_star(self, new_state):
		self._setter_access_tracker["leave_a_star"] = {}
		self._leave_a_star = Anchor(new_state)

	@property
	def python_web_framework(self):
		self._getter_access_tracker["python_web_framework"] = {}
		return self._python_web_framework
	@python_web_framework.setter
	def python_web_framework(self, new_state):
		self._setter_access_tracker["python_web_framework"] = {}
		self._python_web_framework = TextBox(new_state)

	@property
	def sub_title(self):
		self._getter_access_tracker["sub_title"] = {}
		return self._sub_title
	@sub_title.setter
	def sub_title(self, new_state):
		self._setter_access_tracker["sub_title"] = {}
		self._sub_title = TextBox(new_state)

	@property
	def Video1(self):
		self._getter_access_tracker["Video1"] = {}
		return self._Video1
	@Video1.setter
	def Video1(self, new_state):
		self._setter_access_tracker["Video1"] = {}
		self._Video1 = Video(new_state)

	@property
	def footer(self):
		self._getter_access_tracker["footer"] = {}
		return self._footer
	@footer.setter
	def footer(self, new_state):
		self._setter_access_tracker["footer"] = {}
		self._footer = Flex(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def footer_logo(self):
		self._getter_access_tracker["footer_logo"] = {}
		return self._footer_logo
	@footer_logo.setter
	def footer_logo(self, new_state):
		self._setter_access_tracker["footer_logo"] = {}
		self._footer_logo = Flex(new_state)

	@property
	def social_icons(self):
		self._getter_access_tracker["social_icons"] = {}
		return self._social_icons
	@social_icons.setter
	def social_icons(self, new_state):
		self._setter_access_tracker["social_icons"] = {}
		self._social_icons = Flex(new_state)

	@property
	def anchor_github(self):
		self._getter_access_tracker["anchor_github"] = {}
		return self._anchor_github
	@anchor_github.setter
	def anchor_github(self, new_state):
		self._setter_access_tracker["anchor_github"] = {}
		self._anchor_github = Anchor(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def anchor_linkedin(self):
		self._getter_access_tracker["anchor_linkedin"] = {}
		return self._anchor_linkedin
	@anchor_linkedin.setter
	def anchor_linkedin(self, new_state):
		self._setter_access_tracker["anchor_linkedin"] = {}
		self._anchor_linkedin = Anchor(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def anchor_twitter(self):
		self._getter_access_tracker["anchor_twitter"] = {}
		return self._anchor_twitter
	@anchor_twitter.setter
	def anchor_twitter(self, new_state):
		self._setter_access_tracker["anchor_twitter"] = {}
		self._anchor_twitter = Anchor(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def footer_row_1(self):
		self._getter_access_tracker["footer_row_1"] = {}
		return self._footer_row_1
	@footer_row_1.setter
	def footer_row_1(self, new_state):
		self._setter_access_tracker["footer_row_1"] = {}
		self._footer_row_1 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"container": self._container,
			"hero": self._hero,
			"navbar": self._navbar,
			"main": self._main,
			"max_width": self._max_width,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"Flex9": self._Flex9,
			"Image1": self._Image1,
			"TextBox2": self._TextBox2,
			"Anchor1": self._Anchor1,
			"TextBox3": self._TextBox3,
			"Anchor2": self._Anchor2,
			"TextBox4": self._TextBox4,
			"Anchor3": self._Anchor3,
			"TextBox5": self._TextBox5,
			"Anchor4": self._Anchor4,
			"TextBox7": self._TextBox7,
			"Anchor5": self._Anchor5,
			"Anchor6": self._Anchor6,
			"Flex10": self._Flex10,
			"TextBox8": self._TextBox8,
			"row_1_hero": self._row_1_hero,
			"open_source": self._open_source,
			"TextBox10": self._TextBox10,
			"Flex12": self._Flex12,
			"leave_a_star": self._leave_a_star,
			"python_web_framework": self._python_web_framework,
			"sub_title": self._sub_title,
			"Video1": self._Video1,
			"footer": self._footer,
			"Anchor8": self._Anchor8,
			"Image2": self._Image2,
			"Anchor9": self._Anchor9,
			"Image3": self._Image3,
			"Image4": self._Image4,
			"TextBox14": self._TextBox14,
			"Flex15": self._Flex15,
			"Anchor10": self._Anchor10,
			"footer_logo": self._footer_logo,
			"social_icons": self._social_icons,
			"anchor_github": self._anchor_github,
			"Image5": self._Image5,
			"Flex18": self._Flex18,
			"Image6": self._Image6,
			"Flex19": self._Flex19,
			"anchor_linkedin": self._anchor_linkedin,
			"Image7": self._Image7,
			"Flex20": self._Flex20,
			"anchor_twitter": self._anchor_twitter,
			"Image8": self._Image8,
			"Flex21": self._Flex21,
			"Anchor14": self._Anchor14,
			"Image9": self._Image9,
			"Flex22": self._Flex22,
			"Anchor15": self._Anchor15,
			"footer_row_1": self._footer_row_1
			}
  
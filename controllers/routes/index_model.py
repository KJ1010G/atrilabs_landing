from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.Image import Image
from atri_react.TextBox import TextBox
from atri_react.Anchor import Anchor
from manifests.DropdownMenu import DropdownMenu
from atri_react.Video import Video


  
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
		self.nav_mid = state["nav_mid"] if "nav_mid" in state else None
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
		self.footer = state["footer"] if "footer" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
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
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.footer_left = state["footer_left"] if "footer_left" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.backed_by_wrapper = state["backed_by_wrapper"] if "backed_by_wrapper" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.DropdownMenu1 = state["DropdownMenu1"] if "DropdownMenu1" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.Anchor26 = state["Anchor26"] if "Anchor26" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.Anchor27 = state["Anchor27"] if "Anchor27" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.Anchor28 = state["Anchor28"] if "Anchor28" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.Anchor29 = state["Anchor29"] if "Anchor29" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.Anchor30 = state["Anchor30"] if "Anchor30" in state else None
		self.menu_wrapper = state["menu_wrapper"] if "menu_wrapper" in state else None
		self.design_partner_main = state["design_partner_main"] if "design_partner_main" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.Anchor31 = state["Anchor31"] if "Anchor31" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.Anchor32 = state["Anchor32"] if "Anchor32" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Anchor33 = state["Anchor33"] if "Anchor33" in state else None
		self.HeroVideo = state["HeroVideo"] if "HeroVideo" in state else None
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
	def nav_mid(self):
		self._getter_access_tracker["nav_mid"] = {}
		return self._nav_mid
	@nav_mid.setter
	def nav_mid(self, new_state):
		self._setter_access_tracker["nav_mid"] = {}
		self._nav_mid = Flex(new_state)

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

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

	@property
	def footer_left(self):
		self._getter_access_tracker["footer_left"] = {}
		return self._footer_left
	@footer_left.setter
	def footer_left(self, new_state):
		self._setter_access_tracker["footer_left"] = {}
		self._footer_left = Flex(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def Anchor18(self):
		self._getter_access_tracker["Anchor18"] = {}
		return self._Anchor18
	@Anchor18.setter
	def Anchor18(self, new_state):
		self._setter_access_tracker["Anchor18"] = {}
		self._Anchor18 = Anchor(new_state)

	@property
	def Anchor19(self):
		self._getter_access_tracker["Anchor19"] = {}
		return self._Anchor19
	@Anchor19.setter
	def Anchor19(self, new_state):
		self._setter_access_tracker["Anchor19"] = {}
		self._Anchor19 = Anchor(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def Anchor20(self):
		self._getter_access_tracker["Anchor20"] = {}
		return self._Anchor20
	@Anchor20.setter
	def Anchor20(self, new_state):
		self._setter_access_tracker["Anchor20"] = {}
		self._Anchor20 = Anchor(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def Anchor24(self):
		self._getter_access_tracker["Anchor24"] = {}
		return self._Anchor24
	@Anchor24.setter
	def Anchor24(self, new_state):
		self._setter_access_tracker["Anchor24"] = {}
		self._Anchor24 = Anchor(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def backed_by_wrapper(self):
		self._getter_access_tracker["backed_by_wrapper"] = {}
		return self._backed_by_wrapper
	@backed_by_wrapper.setter
	def backed_by_wrapper(self, new_state):
		self._setter_access_tracker["backed_by_wrapper"] = {}
		self._backed_by_wrapper = Flex(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def DropdownMenu1(self):
		self._getter_access_tracker["DropdownMenu1"] = {}
		return self._DropdownMenu1
	@DropdownMenu1.setter
	def DropdownMenu1(self, new_state):
		self._setter_access_tracker["DropdownMenu1"] = {}
		self._DropdownMenu1 = DropdownMenu(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

	@property
	def Anchor26(self):
		self._getter_access_tracker["Anchor26"] = {}
		return self._Anchor26
	@Anchor26.setter
	def Anchor26(self, new_state):
		self._setter_access_tracker["Anchor26"] = {}
		self._Anchor26 = Anchor(new_state)

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		self._TextBox38 = TextBox(new_state)

	@property
	def Anchor27(self):
		self._getter_access_tracker["Anchor27"] = {}
		return self._Anchor27
	@Anchor27.setter
	def Anchor27(self, new_state):
		self._setter_access_tracker["Anchor27"] = {}
		self._Anchor27 = Anchor(new_state)

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		self._TextBox39 = TextBox(new_state)

	@property
	def Anchor28(self):
		self._getter_access_tracker["Anchor28"] = {}
		return self._Anchor28
	@Anchor28.setter
	def Anchor28(self, new_state):
		self._setter_access_tracker["Anchor28"] = {}
		self._Anchor28 = Anchor(new_state)

	@property
	def TextBox40(self):
		self._getter_access_tracker["TextBox40"] = {}
		return self._TextBox40
	@TextBox40.setter
	def TextBox40(self, new_state):
		self._setter_access_tracker["TextBox40"] = {}
		self._TextBox40 = TextBox(new_state)

	@property
	def Anchor29(self):
		self._getter_access_tracker["Anchor29"] = {}
		return self._Anchor29
	@Anchor29.setter
	def Anchor29(self, new_state):
		self._setter_access_tracker["Anchor29"] = {}
		self._Anchor29 = Anchor(new_state)

	@property
	def TextBox41(self):
		self._getter_access_tracker["TextBox41"] = {}
		return self._TextBox41
	@TextBox41.setter
	def TextBox41(self, new_state):
		self._setter_access_tracker["TextBox41"] = {}
		self._TextBox41 = TextBox(new_state)

	@property
	def Anchor30(self):
		self._getter_access_tracker["Anchor30"] = {}
		return self._Anchor30
	@Anchor30.setter
	def Anchor30(self, new_state):
		self._setter_access_tracker["Anchor30"] = {}
		self._Anchor30 = Anchor(new_state)

	@property
	def menu_wrapper(self):
		self._getter_access_tracker["menu_wrapper"] = {}
		return self._menu_wrapper
	@menu_wrapper.setter
	def menu_wrapper(self, new_state):
		self._setter_access_tracker["menu_wrapper"] = {}
		self._menu_wrapper = Flex(new_state)

	@property
	def design_partner_main(self):
		self._getter_access_tracker["design_partner_main"] = {}
		return self._design_partner_main
	@design_partner_main.setter
	def design_partner_main(self, new_state):
		self._setter_access_tracker["design_partner_main"] = {}
		self._design_partner_main = Flex(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

	@property
	def Anchor31(self):
		self._getter_access_tracker["Anchor31"] = {}
		return self._Anchor31
	@Anchor31.setter
	def Anchor31(self, new_state):
		self._setter_access_tracker["Anchor31"] = {}
		self._Anchor31 = Anchor(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def Anchor32(self):
		self._getter_access_tracker["Anchor32"] = {}
		return self._Anchor32
	@Anchor32.setter
	def Anchor32(self, new_state):
		self._setter_access_tracker["Anchor32"] = {}
		self._Anchor32 = Anchor(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def Anchor33(self):
		self._getter_access_tracker["Anchor33"] = {}
		return self._Anchor33
	@Anchor33.setter
	def Anchor33(self, new_state):
		self._setter_access_tracker["Anchor33"] = {}
		self._Anchor33 = Anchor(new_state)

	@property
	def HeroVideo(self):
		self._getter_access_tracker["HeroVideo"] = {}
		return self._HeroVideo
	@HeroVideo.setter
	def HeroVideo(self, new_state):
		self._setter_access_tracker["HeroVideo"] = {}
		self._HeroVideo = Video(new_state)
  
	def _to_json_fields(self):
		return {
			"container": self._container,
			"hero": self._hero,
			"navbar": self._navbar,
			"main": self._main,
			"max_width": self._max_width,
			"Flex7": self._Flex7,
			"nav_mid": self._nav_mid,
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
			"footer": self._footer,
			"Anchor8": self._Anchor8,
			"Image2": self._Image2,
			"Anchor9": self._Anchor9,
			"Image3": self._Image3,
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
			"footer_row_1": self._footer_row_1,
			"Flex24": self._Flex24,
			"footer_left": self._footer_left,
			"Flex27": self._Flex27,
			"TextBox15": self._TextBox15,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Anchor16": self._Anchor16,
			"Anchor17": self._Anchor17,
			"TextBox20": self._TextBox20,
			"TextBox21": self._TextBox21,
			"Anchor18": self._Anchor18,
			"Anchor19": self._Anchor19,
			"TextBox22": self._TextBox22,
			"Flex31": self._Flex31,
			"TextBox23": self._TextBox23,
			"TextBox24": self._TextBox24,
			"Anchor20": self._Anchor20,
			"Anchor21": self._Anchor21,
			"TextBox25": self._TextBox25,
			"Flex32": self._Flex32,
			"TextBox27": self._TextBox27,
			"Anchor23": self._Anchor23,
			"TextBox28": self._TextBox28,
			"Flex33": self._Flex33,
			"TextBox29": self._TextBox29,
			"Anchor24": self._Anchor24,
			"Image10": self._Image10,
			"TextBox30": self._TextBox30,
			"backed_by_wrapper": self._backed_by_wrapper,
			"TextBox31": self._TextBox31,
			"Image11": self._Image11,
			"DropdownMenu1": self._DropdownMenu1,
			"Flex40": self._Flex40,
			"TextBox37": self._TextBox37,
			"Anchor26": self._Anchor26,
			"TextBox38": self._TextBox38,
			"Anchor27": self._Anchor27,
			"TextBox39": self._TextBox39,
			"Anchor28": self._Anchor28,
			"TextBox40": self._TextBox40,
			"Anchor29": self._Anchor29,
			"TextBox41": self._TextBox41,
			"Anchor30": self._Anchor30,
			"menu_wrapper": self._menu_wrapper,
			"design_partner_main": self._design_partner_main,
			"TextBox42": self._TextBox42,
			"Anchor31": self._Anchor31,
			"Flex43": self._Flex43,
			"Anchor32": self._Anchor32,
			"Image12": self._Image12,
			"Image13": self._Image13,
			"Image15": self._Image15,
			"TextBox44": self._TextBox44,
			"Flex45": self._Flex45,
			"Anchor33": self._Anchor33,
			"HeroVideo": self._HeroVideo
			}
  
from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.TextBox import TextBox
from atri_react.Anchor import Anchor
from manifests.DropdownMenu import DropdownMenu
from atri_react.Image import Image


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.container = state["container"] if "container" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.DropdownMenu1 = state["DropdownMenu1"] if "DropdownMenu1" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.navbar = state["navbar"] if "navbar" in state else None
		self.pricing_container = state["pricing_container"] if "pricing_container" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.TextBox78 = state["TextBox78"] if "TextBox78" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.Anchor22 = state["Anchor22"] if "Anchor22" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.Anchor26 = state["Anchor26"] if "Anchor26" in state else None
		self.Anchor27 = state["Anchor27"] if "Anchor27" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.TextBox83 = state["TextBox83"] if "TextBox83" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.TextBox86 = state["TextBox86"] if "TextBox86" in state else None
		self.TextBox88 = state["TextBox88"] if "TextBox88" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.TextBox89 = state["TextBox89"] if "TextBox89" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.TextBox90 = state["TextBox90"] if "TextBox90" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.TextBox91 = state["TextBox91"] if "TextBox91" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.TextBox92 = state["TextBox92"] if "TextBox92" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.TextBox93 = state["TextBox93"] if "TextBox93" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.TextBox94 = state["TextBox94"] if "TextBox94" in state else None
		self.TextBox95 = state["TextBox95"] if "TextBox95" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.TextBox96 = state["TextBox96"] if "TextBox96" in state else None
		self.Image19 = state["Image19"] if "Image19" in state else None
		self.Image20 = state["Image20"] if "Image20" in state else None
		self.TextBox97 = state["TextBox97"] if "TextBox97" in state else None
		self.TextBox98 = state["TextBox98"] if "TextBox98" in state else None
		self.Image21 = state["Image21"] if "Image21" in state else None
		self.Image22 = state["Image22"] if "Image22" in state else None
		self.TextBox99 = state["TextBox99"] if "TextBox99" in state else None
		self.TextBox100 = state["TextBox100"] if "TextBox100" in state else None
		self.TextBox101 = state["TextBox101"] if "TextBox101" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.TextBox102 = state["TextBox102"] if "TextBox102" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.TextBox103 = state["TextBox103"] if "TextBox103" in state else None
		self.Image23 = state["Image23"] if "Image23" in state else None
		self.Image24 = state["Image24"] if "Image24" in state else None
		self.TextBox104 = state["TextBox104"] if "TextBox104" in state else None
		self.TextBox105 = state["TextBox105"] if "TextBox105" in state else None
		self.Image25 = state["Image25"] if "Image25" in state else None
		self.Image26 = state["Image26"] if "Image26" in state else None
		self.TextBox106 = state["TextBox106"] if "TextBox106" in state else None
		self.TextBox108 = state["TextBox108"] if "TextBox108" in state else None
		self.Image28 = state["Image28"] if "Image28" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.TextBox109 = state["TextBox109"] if "TextBox109" in state else None
		self.TextBox111 = state["TextBox111"] if "TextBox111" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Flex68 = state["Flex68"] if "Flex68" in state else None
		self.Flex69 = state["Flex69"] if "Flex69" in state else None
		self.Image29 = state["Image29"] if "Image29" in state else None
		self.TextBox112 = state["TextBox112"] if "TextBox112" in state else None
		self.Flex70 = state["Flex70"] if "Flex70" in state else None
		self.TextBox114 = state["TextBox114"] if "TextBox114" in state else None
		self.Flex72 = state["Flex72"] if "Flex72" in state else None
		self.TextBox115 = state["TextBox115"] if "TextBox115" in state else None
		self.Flex73 = state["Flex73"] if "Flex73" in state else None
		self.Anchor28 = state["Anchor28"] if "Anchor28" in state else None
		self.Anchor30 = state["Anchor30"] if "Anchor30" in state else None
		self.TextBox116 = state["TextBox116"] if "TextBox116" in state else None
		self.Flex75 = state["Flex75"] if "Flex75" in state else None
		self.Anchor31 = state["Anchor31"] if "Anchor31" in state else None
		self.TextBox118 = state["TextBox118"] if "TextBox118" in state else None
		self.Flex77 = state["Flex77"] if "Flex77" in state else None
		self.Anchor32 = state["Anchor32"] if "Anchor32" in state else None
		self.TextBox131 = state["TextBox131"] if "TextBox131" in state else None
		self.TextBox132 = state["TextBox132"] if "TextBox132" in state else None
		self.TextBox133 = state["TextBox133"] if "TextBox133" in state else None
		self.TextBox134 = state["TextBox134"] if "TextBox134" in state else None
		self.TextBox135 = state["TextBox135"] if "TextBox135" in state else None
		self.TextBox136 = state["TextBox136"] if "TextBox136" in state else None
		self.TextBox137 = state["TextBox137"] if "TextBox137" in state else None
		self.TextBox138 = state["TextBox138"] if "TextBox138" in state else None
		self.TextBox139 = state["TextBox139"] if "TextBox139" in state else None
		self.Anchor41 = state["Anchor41"] if "Anchor41" in state else None
		self.TextBox140 = state["TextBox140"] if "TextBox140" in state else None
		self.Anchor42 = state["Anchor42"] if "Anchor42" in state else None
		self.Anchor43 = state["Anchor43"] if "Anchor43" in state else None
		self.Anchor44 = state["Anchor44"] if "Anchor44" in state else None
		self.TextBox141 = state["TextBox141"] if "TextBox141" in state else None
		self.Anchor45 = state["Anchor45"] if "Anchor45" in state else None
		self.Anchor46 = state["Anchor46"] if "Anchor46" in state else None
		self.Anchor47 = state["Anchor47"] if "Anchor47" in state else None
		self.Anchor48 = state["Anchor48"] if "Anchor48" in state else None
		self.TextBox142 = state["TextBox142"] if "TextBox142" in state else None
		self.Flex83 = state["Flex83"] if "Flex83" in state else None
		self.Flex84 = state["Flex84"] if "Flex84" in state else None
		self.Flex85 = state["Flex85"] if "Flex85" in state else None
		self.Flex86 = state["Flex86"] if "Flex86" in state else None
		self.Flex87 = state["Flex87"] if "Flex87" in state else None
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
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def DropdownMenu1(self):
		self._getter_access_tracker["DropdownMenu1"] = {}
		return self._DropdownMenu1
	@DropdownMenu1.setter
	def DropdownMenu1(self, new_state):
		self._setter_access_tracker["DropdownMenu1"] = {}
		self._DropdownMenu1 = DropdownMenu(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def Anchor12(self):
		self._getter_access_tracker["Anchor12"] = {}
		return self._Anchor12
	@Anchor12.setter
	def Anchor12(self, new_state):
		self._setter_access_tracker["Anchor12"] = {}
		self._Anchor12 = Anchor(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

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
	def navbar(self):
		self._getter_access_tracker["navbar"] = {}
		return self._navbar
	@navbar.setter
	def navbar(self, new_state):
		self._setter_access_tracker["navbar"] = {}
		self._navbar = Flex(new_state)

	@property
	def pricing_container(self):
		self._getter_access_tracker["pricing_container"] = {}
		return self._pricing_container
	@pricing_container.setter
	def pricing_container(self, new_state):
		self._setter_access_tracker["pricing_container"] = {}
		self._pricing_container = Flex(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

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
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

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
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		self._TextBox78 = TextBox(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def Anchor22(self):
		self._getter_access_tracker["Anchor22"] = {}
		return self._Anchor22
	@Anchor22.setter
	def Anchor22(self, new_state):
		self._setter_access_tracker["Anchor22"] = {}
		self._Anchor22 = Anchor(new_state)

	@property
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

	@property
	def Anchor24(self):
		self._getter_access_tracker["Anchor24"] = {}
		return self._Anchor24
	@Anchor24.setter
	def Anchor24(self, new_state):
		self._setter_access_tracker["Anchor24"] = {}
		self._Anchor24 = Anchor(new_state)

	@property
	def Anchor25(self):
		self._getter_access_tracker["Anchor25"] = {}
		return self._Anchor25
	@Anchor25.setter
	def Anchor25(self, new_state):
		self._setter_access_tracker["Anchor25"] = {}
		self._Anchor25 = Anchor(new_state)

	@property
	def Anchor26(self):
		self._getter_access_tracker["Anchor26"] = {}
		return self._Anchor26
	@Anchor26.setter
	def Anchor26(self, new_state):
		self._setter_access_tracker["Anchor26"] = {}
		self._Anchor26 = Anchor(new_state)

	@property
	def Anchor27(self):
		self._getter_access_tracker["Anchor27"] = {}
		return self._Anchor27
	@Anchor27.setter
	def Anchor27(self, new_state):
		self._setter_access_tracker["Anchor27"] = {}
		self._Anchor27 = Anchor(new_state)

	@property
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		self._Flex39 = Flex(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def TextBox83(self):
		self._getter_access_tracker["TextBox83"] = {}
		return self._TextBox83
	@TextBox83.setter
	def TextBox83(self, new_state):
		self._setter_access_tracker["TextBox83"] = {}
		self._TextBox83 = TextBox(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def Flex42(self):
		self._getter_access_tracker["Flex42"] = {}
		return self._Flex42
	@Flex42.setter
	def Flex42(self, new_state):
		self._setter_access_tracker["Flex42"] = {}
		self._Flex42 = Flex(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		self._Flex46 = Flex(new_state)

	@property
	def TextBox86(self):
		self._getter_access_tracker["TextBox86"] = {}
		return self._TextBox86
	@TextBox86.setter
	def TextBox86(self, new_state):
		self._setter_access_tracker["TextBox86"] = {}
		self._TextBox86 = TextBox(new_state)

	@property
	def TextBox88(self):
		self._getter_access_tracker["TextBox88"] = {}
		return self._TextBox88
	@TextBox88.setter
	def TextBox88(self, new_state):
		self._setter_access_tracker["TextBox88"] = {}
		self._TextBox88 = TextBox(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		self._Flex47 = Flex(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def TextBox89(self):
		self._getter_access_tracker["TextBox89"] = {}
		return self._TextBox89
	@TextBox89.setter
	def TextBox89(self, new_state):
		self._setter_access_tracker["TextBox89"] = {}
		self._TextBox89 = TextBox(new_state)

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		self._Flex48 = Flex(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def TextBox90(self):
		self._getter_access_tracker["TextBox90"] = {}
		return self._TextBox90
	@TextBox90.setter
	def TextBox90(self, new_state):
		self._setter_access_tracker["TextBox90"] = {}
		self._TextBox90 = TextBox(new_state)

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		self._Flex49 = Flex(new_state)

	@property
	def TextBox91(self):
		self._getter_access_tracker["TextBox91"] = {}
		return self._TextBox91
	@TextBox91.setter
	def TextBox91(self, new_state):
		self._setter_access_tracker["TextBox91"] = {}
		self._TextBox91 = TextBox(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def TextBox92(self):
		self._getter_access_tracker["TextBox92"] = {}
		return self._TextBox92
	@TextBox92.setter
	def TextBox92(self, new_state):
		self._setter_access_tracker["TextBox92"] = {}
		self._TextBox92 = TextBox(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def TextBox93(self):
		self._getter_access_tracker["TextBox93"] = {}
		return self._TextBox93
	@TextBox93.setter
	def TextBox93(self, new_state):
		self._setter_access_tracker["TextBox93"] = {}
		self._TextBox93 = TextBox(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def TextBox94(self):
		self._getter_access_tracker["TextBox94"] = {}
		return self._TextBox94
	@TextBox94.setter
	def TextBox94(self, new_state):
		self._setter_access_tracker["TextBox94"] = {}
		self._TextBox94 = TextBox(new_state)

	@property
	def TextBox95(self):
		self._getter_access_tracker["TextBox95"] = {}
		return self._TextBox95
	@TextBox95.setter
	def TextBox95(self, new_state):
		self._setter_access_tracker["TextBox95"] = {}
		self._TextBox95 = TextBox(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def TextBox96(self):
		self._getter_access_tracker["TextBox96"] = {}
		return self._TextBox96
	@TextBox96.setter
	def TextBox96(self, new_state):
		self._setter_access_tracker["TextBox96"] = {}
		self._TextBox96 = TextBox(new_state)

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		self._Image19 = Image(new_state)

	@property
	def Image20(self):
		self._getter_access_tracker["Image20"] = {}
		return self._Image20
	@Image20.setter
	def Image20(self, new_state):
		self._setter_access_tracker["Image20"] = {}
		self._Image20 = Image(new_state)

	@property
	def TextBox97(self):
		self._getter_access_tracker["TextBox97"] = {}
		return self._TextBox97
	@TextBox97.setter
	def TextBox97(self, new_state):
		self._setter_access_tracker["TextBox97"] = {}
		self._TextBox97 = TextBox(new_state)

	@property
	def TextBox98(self):
		self._getter_access_tracker["TextBox98"] = {}
		return self._TextBox98
	@TextBox98.setter
	def TextBox98(self, new_state):
		self._setter_access_tracker["TextBox98"] = {}
		self._TextBox98 = TextBox(new_state)

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		self._Image21 = Image(new_state)

	@property
	def Image22(self):
		self._getter_access_tracker["Image22"] = {}
		return self._Image22
	@Image22.setter
	def Image22(self, new_state):
		self._setter_access_tracker["Image22"] = {}
		self._Image22 = Image(new_state)

	@property
	def TextBox99(self):
		self._getter_access_tracker["TextBox99"] = {}
		return self._TextBox99
	@TextBox99.setter
	def TextBox99(self, new_state):
		self._setter_access_tracker["TextBox99"] = {}
		self._TextBox99 = TextBox(new_state)

	@property
	def TextBox100(self):
		self._getter_access_tracker["TextBox100"] = {}
		return self._TextBox100
	@TextBox100.setter
	def TextBox100(self, new_state):
		self._setter_access_tracker["TextBox100"] = {}
		self._TextBox100 = TextBox(new_state)

	@property
	def TextBox101(self):
		self._getter_access_tracker["TextBox101"] = {}
		return self._TextBox101
	@TextBox101.setter
	def TextBox101(self, new_state):
		self._setter_access_tracker["TextBox101"] = {}
		self._TextBox101 = TextBox(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def TextBox102(self):
		self._getter_access_tracker["TextBox102"] = {}
		return self._TextBox102
	@TextBox102.setter
	def TextBox102(self, new_state):
		self._setter_access_tracker["TextBox102"] = {}
		self._TextBox102 = TextBox(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def TextBox103(self):
		self._getter_access_tracker["TextBox103"] = {}
		return self._TextBox103
	@TextBox103.setter
	def TextBox103(self, new_state):
		self._setter_access_tracker["TextBox103"] = {}
		self._TextBox103 = TextBox(new_state)

	@property
	def Image23(self):
		self._getter_access_tracker["Image23"] = {}
		return self._Image23
	@Image23.setter
	def Image23(self, new_state):
		self._setter_access_tracker["Image23"] = {}
		self._Image23 = Image(new_state)

	@property
	def Image24(self):
		self._getter_access_tracker["Image24"] = {}
		return self._Image24
	@Image24.setter
	def Image24(self, new_state):
		self._setter_access_tracker["Image24"] = {}
		self._Image24 = Image(new_state)

	@property
	def TextBox104(self):
		self._getter_access_tracker["TextBox104"] = {}
		return self._TextBox104
	@TextBox104.setter
	def TextBox104(self, new_state):
		self._setter_access_tracker["TextBox104"] = {}
		self._TextBox104 = TextBox(new_state)

	@property
	def TextBox105(self):
		self._getter_access_tracker["TextBox105"] = {}
		return self._TextBox105
	@TextBox105.setter
	def TextBox105(self, new_state):
		self._setter_access_tracker["TextBox105"] = {}
		self._TextBox105 = TextBox(new_state)

	@property
	def Image25(self):
		self._getter_access_tracker["Image25"] = {}
		return self._Image25
	@Image25.setter
	def Image25(self, new_state):
		self._setter_access_tracker["Image25"] = {}
		self._Image25 = Image(new_state)

	@property
	def Image26(self):
		self._getter_access_tracker["Image26"] = {}
		return self._Image26
	@Image26.setter
	def Image26(self, new_state):
		self._setter_access_tracker["Image26"] = {}
		self._Image26 = Image(new_state)

	@property
	def TextBox106(self):
		self._getter_access_tracker["TextBox106"] = {}
		return self._TextBox106
	@TextBox106.setter
	def TextBox106(self, new_state):
		self._setter_access_tracker["TextBox106"] = {}
		self._TextBox106 = TextBox(new_state)

	@property
	def TextBox108(self):
		self._getter_access_tracker["TextBox108"] = {}
		return self._TextBox108
	@TextBox108.setter
	def TextBox108(self, new_state):
		self._setter_access_tracker["TextBox108"] = {}
		self._TextBox108 = TextBox(new_state)

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		self._Image28 = Image(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

	@property
	def TextBox109(self):
		self._getter_access_tracker["TextBox109"] = {}
		return self._TextBox109
	@TextBox109.setter
	def TextBox109(self, new_state):
		self._setter_access_tracker["TextBox109"] = {}
		self._TextBox109 = TextBox(new_state)

	@property
	def TextBox111(self):
		self._getter_access_tracker["TextBox111"] = {}
		return self._TextBox111
	@TextBox111.setter
	def TextBox111(self, new_state):
		self._setter_access_tracker["TextBox111"] = {}
		self._TextBox111 = TextBox(new_state)

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		self._Flex68 = Flex(new_state)

	@property
	def Flex69(self):
		self._getter_access_tracker["Flex69"] = {}
		return self._Flex69
	@Flex69.setter
	def Flex69(self, new_state):
		self._setter_access_tracker["Flex69"] = {}
		self._Flex69 = Flex(new_state)

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		self._Image29 = Image(new_state)

	@property
	def TextBox112(self):
		self._getter_access_tracker["TextBox112"] = {}
		return self._TextBox112
	@TextBox112.setter
	def TextBox112(self, new_state):
		self._setter_access_tracker["TextBox112"] = {}
		self._TextBox112 = TextBox(new_state)

	@property
	def Flex70(self):
		self._getter_access_tracker["Flex70"] = {}
		return self._Flex70
	@Flex70.setter
	def Flex70(self, new_state):
		self._setter_access_tracker["Flex70"] = {}
		self._Flex70 = Flex(new_state)

	@property
	def TextBox114(self):
		self._getter_access_tracker["TextBox114"] = {}
		return self._TextBox114
	@TextBox114.setter
	def TextBox114(self, new_state):
		self._setter_access_tracker["TextBox114"] = {}
		self._TextBox114 = TextBox(new_state)

	@property
	def Flex72(self):
		self._getter_access_tracker["Flex72"] = {}
		return self._Flex72
	@Flex72.setter
	def Flex72(self, new_state):
		self._setter_access_tracker["Flex72"] = {}
		self._Flex72 = Flex(new_state)

	@property
	def TextBox115(self):
		self._getter_access_tracker["TextBox115"] = {}
		return self._TextBox115
	@TextBox115.setter
	def TextBox115(self, new_state):
		self._setter_access_tracker["TextBox115"] = {}
		self._TextBox115 = TextBox(new_state)

	@property
	def Flex73(self):
		self._getter_access_tracker["Flex73"] = {}
		return self._Flex73
	@Flex73.setter
	def Flex73(self, new_state):
		self._setter_access_tracker["Flex73"] = {}
		self._Flex73 = Flex(new_state)

	@property
	def Anchor28(self):
		self._getter_access_tracker["Anchor28"] = {}
		return self._Anchor28
	@Anchor28.setter
	def Anchor28(self, new_state):
		self._setter_access_tracker["Anchor28"] = {}
		self._Anchor28 = Anchor(new_state)

	@property
	def Anchor30(self):
		self._getter_access_tracker["Anchor30"] = {}
		return self._Anchor30
	@Anchor30.setter
	def Anchor30(self, new_state):
		self._setter_access_tracker["Anchor30"] = {}
		self._Anchor30 = Anchor(new_state)

	@property
	def TextBox116(self):
		self._getter_access_tracker["TextBox116"] = {}
		return self._TextBox116
	@TextBox116.setter
	def TextBox116(self, new_state):
		self._setter_access_tracker["TextBox116"] = {}
		self._TextBox116 = TextBox(new_state)

	@property
	def Flex75(self):
		self._getter_access_tracker["Flex75"] = {}
		return self._Flex75
	@Flex75.setter
	def Flex75(self, new_state):
		self._setter_access_tracker["Flex75"] = {}
		self._Flex75 = Flex(new_state)

	@property
	def Anchor31(self):
		self._getter_access_tracker["Anchor31"] = {}
		return self._Anchor31
	@Anchor31.setter
	def Anchor31(self, new_state):
		self._setter_access_tracker["Anchor31"] = {}
		self._Anchor31 = Anchor(new_state)

	@property
	def TextBox118(self):
		self._getter_access_tracker["TextBox118"] = {}
		return self._TextBox118
	@TextBox118.setter
	def TextBox118(self, new_state):
		self._setter_access_tracker["TextBox118"] = {}
		self._TextBox118 = TextBox(new_state)

	@property
	def Flex77(self):
		self._getter_access_tracker["Flex77"] = {}
		return self._Flex77
	@Flex77.setter
	def Flex77(self, new_state):
		self._setter_access_tracker["Flex77"] = {}
		self._Flex77 = Flex(new_state)

	@property
	def Anchor32(self):
		self._getter_access_tracker["Anchor32"] = {}
		return self._Anchor32
	@Anchor32.setter
	def Anchor32(self, new_state):
		self._setter_access_tracker["Anchor32"] = {}
		self._Anchor32 = Anchor(new_state)

	@property
	def TextBox131(self):
		self._getter_access_tracker["TextBox131"] = {}
		return self._TextBox131
	@TextBox131.setter
	def TextBox131(self, new_state):
		self._setter_access_tracker["TextBox131"] = {}
		self._TextBox131 = TextBox(new_state)

	@property
	def TextBox132(self):
		self._getter_access_tracker["TextBox132"] = {}
		return self._TextBox132
	@TextBox132.setter
	def TextBox132(self, new_state):
		self._setter_access_tracker["TextBox132"] = {}
		self._TextBox132 = TextBox(new_state)

	@property
	def TextBox133(self):
		self._getter_access_tracker["TextBox133"] = {}
		return self._TextBox133
	@TextBox133.setter
	def TextBox133(self, new_state):
		self._setter_access_tracker["TextBox133"] = {}
		self._TextBox133 = TextBox(new_state)

	@property
	def TextBox134(self):
		self._getter_access_tracker["TextBox134"] = {}
		return self._TextBox134
	@TextBox134.setter
	def TextBox134(self, new_state):
		self._setter_access_tracker["TextBox134"] = {}
		self._TextBox134 = TextBox(new_state)

	@property
	def TextBox135(self):
		self._getter_access_tracker["TextBox135"] = {}
		return self._TextBox135
	@TextBox135.setter
	def TextBox135(self, new_state):
		self._setter_access_tracker["TextBox135"] = {}
		self._TextBox135 = TextBox(new_state)

	@property
	def TextBox136(self):
		self._getter_access_tracker["TextBox136"] = {}
		return self._TextBox136
	@TextBox136.setter
	def TextBox136(self, new_state):
		self._setter_access_tracker["TextBox136"] = {}
		self._TextBox136 = TextBox(new_state)

	@property
	def TextBox137(self):
		self._getter_access_tracker["TextBox137"] = {}
		return self._TextBox137
	@TextBox137.setter
	def TextBox137(self, new_state):
		self._setter_access_tracker["TextBox137"] = {}
		self._TextBox137 = TextBox(new_state)

	@property
	def TextBox138(self):
		self._getter_access_tracker["TextBox138"] = {}
		return self._TextBox138
	@TextBox138.setter
	def TextBox138(self, new_state):
		self._setter_access_tracker["TextBox138"] = {}
		self._TextBox138 = TextBox(new_state)

	@property
	def TextBox139(self):
		self._getter_access_tracker["TextBox139"] = {}
		return self._TextBox139
	@TextBox139.setter
	def TextBox139(self, new_state):
		self._setter_access_tracker["TextBox139"] = {}
		self._TextBox139 = TextBox(new_state)

	@property
	def Anchor41(self):
		self._getter_access_tracker["Anchor41"] = {}
		return self._Anchor41
	@Anchor41.setter
	def Anchor41(self, new_state):
		self._setter_access_tracker["Anchor41"] = {}
		self._Anchor41 = Anchor(new_state)

	@property
	def TextBox140(self):
		self._getter_access_tracker["TextBox140"] = {}
		return self._TextBox140
	@TextBox140.setter
	def TextBox140(self, new_state):
		self._setter_access_tracker["TextBox140"] = {}
		self._TextBox140 = TextBox(new_state)

	@property
	def Anchor42(self):
		self._getter_access_tracker["Anchor42"] = {}
		return self._Anchor42
	@Anchor42.setter
	def Anchor42(self, new_state):
		self._setter_access_tracker["Anchor42"] = {}
		self._Anchor42 = Anchor(new_state)

	@property
	def Anchor43(self):
		self._getter_access_tracker["Anchor43"] = {}
		return self._Anchor43
	@Anchor43.setter
	def Anchor43(self, new_state):
		self._setter_access_tracker["Anchor43"] = {}
		self._Anchor43 = Anchor(new_state)

	@property
	def Anchor44(self):
		self._getter_access_tracker["Anchor44"] = {}
		return self._Anchor44
	@Anchor44.setter
	def Anchor44(self, new_state):
		self._setter_access_tracker["Anchor44"] = {}
		self._Anchor44 = Anchor(new_state)

	@property
	def TextBox141(self):
		self._getter_access_tracker["TextBox141"] = {}
		return self._TextBox141
	@TextBox141.setter
	def TextBox141(self, new_state):
		self._setter_access_tracker["TextBox141"] = {}
		self._TextBox141 = TextBox(new_state)

	@property
	def Anchor45(self):
		self._getter_access_tracker["Anchor45"] = {}
		return self._Anchor45
	@Anchor45.setter
	def Anchor45(self, new_state):
		self._setter_access_tracker["Anchor45"] = {}
		self._Anchor45 = Anchor(new_state)

	@property
	def Anchor46(self):
		self._getter_access_tracker["Anchor46"] = {}
		return self._Anchor46
	@Anchor46.setter
	def Anchor46(self, new_state):
		self._setter_access_tracker["Anchor46"] = {}
		self._Anchor46 = Anchor(new_state)

	@property
	def Anchor47(self):
		self._getter_access_tracker["Anchor47"] = {}
		return self._Anchor47
	@Anchor47.setter
	def Anchor47(self, new_state):
		self._setter_access_tracker["Anchor47"] = {}
		self._Anchor47 = Anchor(new_state)

	@property
	def Anchor48(self):
		self._getter_access_tracker["Anchor48"] = {}
		return self._Anchor48
	@Anchor48.setter
	def Anchor48(self, new_state):
		self._setter_access_tracker["Anchor48"] = {}
		self._Anchor48 = Anchor(new_state)

	@property
	def TextBox142(self):
		self._getter_access_tracker["TextBox142"] = {}
		return self._TextBox142
	@TextBox142.setter
	def TextBox142(self, new_state):
		self._setter_access_tracker["TextBox142"] = {}
		self._TextBox142 = TextBox(new_state)

	@property
	def Flex83(self):
		self._getter_access_tracker["Flex83"] = {}
		return self._Flex83
	@Flex83.setter
	def Flex83(self, new_state):
		self._setter_access_tracker["Flex83"] = {}
		self._Flex83 = Flex(new_state)

	@property
	def Flex84(self):
		self._getter_access_tracker["Flex84"] = {}
		return self._Flex84
	@Flex84.setter
	def Flex84(self, new_state):
		self._setter_access_tracker["Flex84"] = {}
		self._Flex84 = Flex(new_state)

	@property
	def Flex85(self):
		self._getter_access_tracker["Flex85"] = {}
		return self._Flex85
	@Flex85.setter
	def Flex85(self, new_state):
		self._setter_access_tracker["Flex85"] = {}
		self._Flex85 = Flex(new_state)

	@property
	def Flex86(self):
		self._getter_access_tracker["Flex86"] = {}
		return self._Flex86
	@Flex86.setter
	def Flex86(self, new_state):
		self._setter_access_tracker["Flex86"] = {}
		self._Flex86 = Flex(new_state)

	@property
	def Flex87(self):
		self._getter_access_tracker["Flex87"] = {}
		return self._Flex87
	@Flex87.setter
	def Flex87(self, new_state):
		self._setter_access_tracker["Flex87"] = {}
		self._Flex87 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"container": self._container,
			"TextBox2": self._TextBox2,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"Anchor1": self._Anchor1,
			"Anchor2": self._Anchor2,
			"Anchor3": self._Anchor3,
			"Anchor4": self._Anchor4,
			"Anchor5": self._Anchor5,
			"Flex2": self._Flex2,
			"DropdownMenu1": self._DropdownMenu1,
			"TextBox8": self._TextBox8,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"TextBox11": self._TextBox11,
			"TextBox12": self._TextBox12,
			"Image1": self._Image1,
			"Flex4": self._Flex4,
			"Anchor7": self._Anchor7,
			"Anchor8": self._Anchor8,
			"Anchor9": self._Anchor9,
			"Anchor10": self._Anchor10,
			"Anchor11": self._Anchor11,
			"Anchor12": self._Anchor12,
			"Flex5": self._Flex5,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"navbar": self._navbar,
			"pricing_container": self._pricing_container,
			"Flex11": self._Flex11,
			"Flex12": self._Flex12,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"Flex15": self._Flex15,
			"Image2": self._Image2,
			"Image3": self._Image3,
			"Image4": self._Image4,
			"Image5": self._Image5,
			"Image6": self._Image6,
			"TextBox78": self._TextBox78,
			"Image7": self._Image7,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"Image8": self._Image8,
			"Anchor21": self._Anchor21,
			"Anchor22": self._Anchor22,
			"Anchor23": self._Anchor23,
			"Anchor24": self._Anchor24,
			"Anchor25": self._Anchor25,
			"Anchor26": self._Anchor26,
			"Anchor27": self._Anchor27,
			"Flex39": self._Flex39,
			"Flex40": self._Flex40,
			"TextBox83": self._TextBox83,
			"Image9": self._Image9,
			"Flex42": self._Flex42,
			"Flex43": self._Flex43,
			"Flex44": self._Flex44,
			"Image10": self._Image10,
			"Image12": self._Image12,
			"Flex46": self._Flex46,
			"TextBox86": self._TextBox86,
			"TextBox88": self._TextBox88,
			"Image13": self._Image13,
			"Flex47": self._Flex47,
			"Image14": self._Image14,
			"TextBox89": self._TextBox89,
			"Flex48": self._Flex48,
			"Image15": self._Image15,
			"TextBox90": self._TextBox90,
			"Flex49": self._Flex49,
			"TextBox91": self._TextBox91,
			"Image16": self._Image16,
			"Flex50": self._Flex50,
			"TextBox92": self._TextBox92,
			"Flex51": self._Flex51,
			"TextBox93": self._TextBox93,
			"Image17": self._Image17,
			"TextBox94": self._TextBox94,
			"TextBox95": self._TextBox95,
			"Image18": self._Image18,
			"TextBox96": self._TextBox96,
			"Image19": self._Image19,
			"Image20": self._Image20,
			"TextBox97": self._TextBox97,
			"TextBox98": self._TextBox98,
			"Image21": self._Image21,
			"Image22": self._Image22,
			"TextBox99": self._TextBox99,
			"TextBox100": self._TextBox100,
			"TextBox101": self._TextBox101,
			"Flex52": self._Flex52,
			"Flex53": self._Flex53,
			"Flex54": self._Flex54,
			"Flex55": self._Flex55,
			"Flex56": self._Flex56,
			"Flex57": self._Flex57,
			"Flex58": self._Flex58,
			"Flex59": self._Flex59,
			"TextBox102": self._TextBox102,
			"Flex60": self._Flex60,
			"TextBox103": self._TextBox103,
			"Image23": self._Image23,
			"Image24": self._Image24,
			"TextBox104": self._TextBox104,
			"TextBox105": self._TextBox105,
			"Image25": self._Image25,
			"Image26": self._Image26,
			"TextBox106": self._TextBox106,
			"TextBox108": self._TextBox108,
			"Image28": self._Image28,
			"Flex61": self._Flex61,
			"Flex62": self._Flex62,
			"Flex63": self._Flex63,
			"Flex64": self._Flex64,
			"Flex66": self._Flex66,
			"TextBox109": self._TextBox109,
			"TextBox111": self._TextBox111,
			"Flex67": self._Flex67,
			"Flex68": self._Flex68,
			"Flex69": self._Flex69,
			"Image29": self._Image29,
			"TextBox112": self._TextBox112,
			"Flex70": self._Flex70,
			"TextBox114": self._TextBox114,
			"Flex72": self._Flex72,
			"TextBox115": self._TextBox115,
			"Flex73": self._Flex73,
			"Anchor28": self._Anchor28,
			"Anchor30": self._Anchor30,
			"TextBox116": self._TextBox116,
			"Flex75": self._Flex75,
			"Anchor31": self._Anchor31,
			"TextBox118": self._TextBox118,
			"Flex77": self._Flex77,
			"Anchor32": self._Anchor32,
			"TextBox131": self._TextBox131,
			"TextBox132": self._TextBox132,
			"TextBox133": self._TextBox133,
			"TextBox134": self._TextBox134,
			"TextBox135": self._TextBox135,
			"TextBox136": self._TextBox136,
			"TextBox137": self._TextBox137,
			"TextBox138": self._TextBox138,
			"TextBox139": self._TextBox139,
			"Anchor41": self._Anchor41,
			"TextBox140": self._TextBox140,
			"Anchor42": self._Anchor42,
			"Anchor43": self._Anchor43,
			"Anchor44": self._Anchor44,
			"TextBox141": self._TextBox141,
			"Anchor45": self._Anchor45,
			"Anchor46": self._Anchor46,
			"Anchor47": self._Anchor47,
			"Anchor48": self._Anchor48,
			"TextBox142": self._TextBox142,
			"Flex83": self._Flex83,
			"Flex84": self._Flex84,
			"Flex85": self._Flex85,
			"Flex86": self._Flex86,
			"Flex87": self._Flex87
			}
  
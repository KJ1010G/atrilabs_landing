import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "DropdownMenu",
	acceptsChild: () => {
		return 0;
	},
});

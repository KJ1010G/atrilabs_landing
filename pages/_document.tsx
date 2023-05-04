import { AtriScripts } from "@atrilabs/atri-app-core";
import { Main } from "@atrilabs/atri-app-core";

// used only server side
export default function Document() {
	return (
		<html>
			<head>
				<link rel="icon" type="image/x-icon" href="/favicon.ico"></link>
				<meta
					name="viewport"
					content="width=device-width, initial-scale=1"
				></meta>
				<title>Atri TEST Labs</title>
				<AtriScripts />
			</head>
			<body>
				<Main />
			</body>
		</html>
	);
}

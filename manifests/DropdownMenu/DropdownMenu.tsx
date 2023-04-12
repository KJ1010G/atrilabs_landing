import { ReactComponent as Icon } from "./hamburger.svg";
import React, { useCallback, useState } from "react";

const DropdownMenu = React.forwardRef<
	HTMLDivElement,
	{
		className: string;
		styles: React.CSSProperties;
		children: React.ReactNode[];
	}
>((props, ref) => {
	const [open, setOpen] = useState<boolean>(false);
	const onClickCb = useCallback(() => {
		setOpen((open) => !open);
	}, []);
	return (
		<div>
			<div
				ref={ref}
				className={props.className}
				style={{ ...props.styles, position: "relative" }}
				onClick={onClickCb}
			>
				<Icon />
				<div
					style={{
						position: "absolute",
						top: "2em",
						right: "0",
					}}
				>
					{open ? props.children : null}
				</div>
			</div>
		</div>
	);
});

export default DropdownMenu;

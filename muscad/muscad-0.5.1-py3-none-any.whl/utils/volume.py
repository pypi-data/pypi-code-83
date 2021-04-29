from muscad import Cube, E, EE, Part, calc
from muscad.utils.fillet import Chamfer, Fillet


class Volume(Part):
    def init(  # type: ignore[override]
        self,
        *,
        left: float = None,
        center_x: float = None,
        right: float = None,
        width: float = None,
        back: float = None,
        center_y: float = None,
        front: float = None,
        depth: float = None,
        bottom: float = None,
        center_z: float = None,
        top: float = None,
        height: float = None,
    ):
        self._left, self._center_x, self._right, self._width = calc(
            left, center_x, right, width
        )
        self._back, self._center_y, self._front, self._depth = calc(
            back, center_y, front, depth
        )
        self._bottom, self._center_z, self._top, self._height = calc(
            bottom, center_z, top, height
        )
        self.volume = Cube(self.width, self.depth, self.height).align(
            center_x=self.center_x,
            center_y=self.center_y,
            center_z=self.center_z,
        )

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def back(self):
        return self._back

    @property
    def front(self):
        return self._front

    @property
    def bottom(self):
        return self._bottom

    @property
    def top(self):
        return self._top

    def _cut_width_edges(
        self, part, *, back=False, front=False, bottom=False, top=False
    ):
        if not (back or front):
            back = front = True
        if not (bottom or top):
            bottom = top = True

        if front and top:
            self.front_top_chamfer = ~part.x_rotate(90).align(
                center_x=self.center_x, front=self.front + E, top=self.top + E
            )
        if front and bottom:
            self.front_bottom_chamfer = ~part.x_rotate(0).align(
                center_x=self.center_x,
                front=self.front + E,
                bottom=self.bottom - E,
            )
        if back and bottom:
            self.back_bottom_chamfer = ~part.x_rotate(-90).align(
                center_x=self.center_x,
                back=self.back - E,
                bottom=self.bottom - E,
            )
        if back and top:
            self.back_top_chamfer = ~part.x_rotate(180).align(
                center_x=self.center_x, back=self.back - E, top=self.top + E
            )
        return self

    def _cut_depth_edges(
        self, part, *, left=False, right=False, bottom=False, top=False
    ):
        if not (left or right):
            left = right = True
        if not (bottom or top):
            bottom = top = True

        if top and right:
            self.top_right_chamfer = ~part.y_rotate(0).align(
                right=self.right + E, center_y=self.center_y, top=self.top + E
            )
        if bottom and right:
            self.bottom_right_chamfer = ~part.y_rotate(90).align(
                right=self.right + E,
                center_y=self.center_y,
                bottom=self.bottom - E,
            )
        if bottom and left:
            self.bottom_left_chamfer = ~part.y_rotate(180).align(
                left=self.left - E,
                center_y=self.center_y,
                bottom=self.bottom - E,
            )
        if top and left:
            self.top_left_chamfer = ~part.y_rotate(-90).align(
                left=self.left - E, center_y=self.center_y, top=self.top + E
            )

    def _cut_height_edges(
        self, part, *, left=False, right=False, back=False, front=False
    ):
        if not (left or right):
            left = right = True
        if not (front or back):
            back = front = True

        if front and right:
            self.front_right_chamfer = ~part.z_rotate(0).align(
                right=self.right + E,
                front=self.front + E,
                center_z=self.center_z,
            )
        if back and right:
            self.back_right_chamfer = ~part.z_rotate(-90).align(
                right=self.right + E,
                back=self.back - E,
                center_z=self.center_z,
            )
        if back and left:
            self.back_left_chamfer = ~part.z_rotate(180).align(
                left=self.left - E, back=self.back - E, center_z=self.center_z
            )
        if front and left:
            self.front_left_chamfer = ~part.z_rotate(90).align(
                left=self.left - E,
                front=self.front + E,
                center_z=self.center_z,
            )

    def chamfer_width(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        chamfer = Chamfer(self.width + EE, r).y_rotate(90)
        self._cut_width_edges(
            chamfer, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def chamfer_depth(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        chamfer = Chamfer(self.depth + EE, r).x_rotate(90)
        self._cut_depth_edges(
            chamfer, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def chamfer_height(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        chamfer = Chamfer(self.height + EE, r)
        self._cut_height_edges(
            chamfer, left=left, right=right, front=front, back=back
        )
        return self

    def chamfer_all(self, r=2):
        return self.chamfer_depth(r).chamfer_height(r).chamfer_width(r)

    def fillet_width(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        fillet = Fillet(r).linear_extrude(self.width + EE).y_rotate(90)
        self._cut_width_edges(
            fillet, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def fillet_depth(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        fillet = Fillet(r).linear_extrude(self.depth + EE).x_rotate(90)
        self._cut_depth_edges(
            fillet, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def fillet_height(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        fillet = Fillet(r).linear_extrude(self.height + EE)
        self._cut_height_edges(
            fillet, left=left, right=right, front=front, back=back
        )
        return self

    def fillet_all(self, r=2):
        return self.fillet_depth(r).fillet_height(r).fillet_width(r)

    def _add_left_edges(
        self, part, *, back=False, front=False, bottom=False, top=False
    ):
        if not (back or front or bottom or top):
            back = front = bottom = top = True

        if top:
            self.left_top_chamfer = (
                part.y_linear_extrude(self.depth)
                .top_to_bottom()
                .align(
                    left=self.left, center_y=self.center_y, bottom=self.top - E
                )
            )
        if bottom:
            self.left_bottom_chamfer = part.y_linear_extrude(self.depth).align(
                left=self.left,
                center_y=self.center_y,
                top=self.bottom + E,
            )
        if back:
            self.left_back_chamfer = (
                part.z_linear_extrude(self.height)
                .right_to_front()
                .align(
                    left=self.left,
                    front=self.back + E,
                    center_z=self.center_z,
                )
            )
        if front:
            self.left_front_chamfer = (
                part.z_linear_extrude(self.height)
                .front_to_back()
                .align(
                    left=self.left,
                    back=self.front - E,
                    center_z=self.center_z,
                )
            )
        return self

    def _add_right_edges(
        self, part, *, back=False, front=False, bottom=False, top=False
    ):
        if not (back or front or bottom or top):
            back = front = bottom = top = True

        if top:
            self.right_top_chamfer = (
                part.y_linear_extrude(self.depth)
                .top_to_bottom()
                .right_to_left()
                .align(
                    right=self.right,
                    center_y=self.center_y,
                    bottom=self.top - E,
                )
                .misc()
            )
        if bottom:
            self.right_bottom_chamfer = (
                part.y_linear_extrude(self.depth)
                .left_to_right()
                .align(
                    right=self.right,
                    center_y=self.center_y,
                    top=self.bottom + E,
                )
                .misc()
            )
        if back:
            self.right_back_chamfer = (
                part.z_linear_extrude(self.height)
                .align(
                    right=self.right,
                    front=self.back + E,
                    center_z=self.center_z,
                )
                .misc()
            )
        if front:
            self.right_front_chamfer = (
                part.z_linear_extrude(self.height)
                .right_to_back()
                .align(
                    right=self.right,
                    back=self.front - E,
                    center_z=self.center_z,
                )
                .misc()
            )
        return self

    def _add_back_edges(
        self, part, *, left=False, right=False, bottom=False, top=False
    ):
        if not (left or right or bottom or top):
            left = right = bottom = top = True

        if top:
            self.back_top_chamfer = (
                part.x_linear_extrude(self.width)
                .top_to_bottom()
                .align(
                    center_x=self.center_x, back=self.back, bottom=self.top - E
                )
                .misc()
            )
        if bottom:
            self.back_bottom_chamfer = (
                part.x_linear_extrude(self.width)
                .top_to_back()
                .align(
                    center_x=self.center_x,
                    back=self.back,
                    top=self.bottom + E,
                )
                .misc()
            )
        if right:
            self.back_right_chamfer = (
                part.z_linear_extrude(self.height)
                .right_to_left()
                .align(
                    left=self.right - E,
                    back=self.back,
                    center_z=self.center_z,
                )
            )
        if left:
            self.back_left_chamfer = (
                part.z_linear_extrude(self.height)
                .front_to_right()
                .align(
                    right=self.left - E,
                    back=self.back,
                    center_z=self.center_z,
                )
            )

    def _add_front_edges(
        self, part, *, left=False, right=False, bottom=False, top=False
    ):
        if not (left or right or bottom or top):
            left = right = bottom = top = True

        if top:
            self.front_top_chamfer = (
                part.x_linear_extrude(self.width)
                .back_to_top()
                .align(
                    center_x=self.center_x,
                    front=self.front,
                    bottom=self.top - E,
                )
                .misc()
            )
        if bottom:
            self.front_bottom_chamfer = (
                part.x_linear_extrude(self.width)
                .align(
                    center_x=self.center_x,
                    front=self.front,
                    top=self.bottom + E,
                )
                .misc()
            )
        if right:
            self.front_right_chamfer = (
                part.z_linear_extrude(self.height)
                .front_to_left()
                .align(
                    left=self.right - E,
                    front=self.front,
                    center_z=self.center_z,
                )
                .misc()
            )
        if left:
            self.front_left_chamfer = (
                part.z_linear_extrude(self.height)
                .align(
                    right=self.left - E,
                    front=self.front,
                    center_z=self.center_z,
                )
                .misc()
            )

    def _add_top_edges(
        self, part, *, left=False, right=False, back=False, front=False
    ):
        if not (left or right or back or front):
            left = right = back = front = True

        if front:
            self.top_front_chamfer = (
                part.x_linear_extrude(self.width)
                .top_to_back()
                .align(
                    center_x=self.center_x, back=self.front - E, top=self.top
                )
                .misc()
            )
        if back:
            self.top_back_chamfer = (
                part.x_linear_extrude(self.width)
                .align(
                    center_x=self.center_x,
                    front=self.back + E,
                    top=self.top,
                )
                .misc()
            )
        if right:
            self.top_right_chamfer = (
                part.y_linear_extrude(self.depth)
                .align(
                    left=self.right - E,
                    center_y=self.center_y,
                    top=self.top,
                )
                .misc()
            )
        if left:
            self.top_left_chamfer = (
                part.y_linear_extrude(self.depth)
                .left_to_right()
                .align(
                    right=self.left - E,
                    center_y=self.center_y,
                    top=self.top,
                )
                .misc()
            )

    def _add_bottom_edges(
        self, part, *, left=False, right=False, back=False, front=False
    ):
        if not (left or right or back or front):
            left = right = back = front = True

        if front:
            self.bottom_front_chamfer = (
                part.x_linear_extrude(self.width)
                .top_to_bottom()
                .align(
                    center_x=self.center_x,
                    back=self.front - E,
                    bottom=self.bottom,
                )
                .misc()
            )
        if back:
            self.bottom_back_chamfer = (
                part.x_linear_extrude(self.width)
                .bottom_to_back()
                .align(
                    center_x=self.center_x,
                    front=self.back + E,
                    bottom=self.bottom,
                )
                .misc()
            )
        if right:
            self.bottom_right_chamfer = (
                part.y_linear_extrude(self.depth)
                .bottom_to_top()
                .align(
                    left=self.right - E,
                    center_y=self.center_y,
                    bottom=self.bottom,
                )
                .misc()
            )
        if left:
            self.bottom_left_chamfer = (
                part.y_linear_extrude(self.width)
                .top_to_bottom()
                .left_to_right()
                .align(
                    right=self.left - E,
                    center_y=self.center_y,
                    bottom=self.bottom,
                )
                .misc()
            )

    def reverse_fillet_left(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        fillet = Fillet(r)
        self._add_left_edges(
            fillet, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def reverse_fillet_right(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        fillet = Fillet(r)
        self._add_right_edges(
            fillet, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def reverse_fillet_back(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        fillet = Fillet(r)
        self._add_back_edges(
            fillet, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def reverse_fillet_front(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        fillet = Fillet(r)
        self._add_front_edges(
            fillet, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def reverse_fillet_bottom(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        fillet = Fillet(r)
        self._add_bottom_edges(
            fillet, left=left, right=right, front=front, back=back
        )
        return self

    def reverse_fillet_top(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        fillet = Fillet(r)
        self._add_top_edges(
            fillet, left=left, right=right, front=front, back=back
        )
        return self

    def reverse_chamfer_left(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        fillet = Chamfer(r)
        self._add_left_edges(
            fillet, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def reverse_chamfer_right(
        self, r=2, *, back=False, front=False, top=False, bottom=False
    ):
        fillet = Chamfer(r)
        self._add_right_edges(
            fillet, back=back, front=front, top=top, bottom=bottom
        )
        return self

    def reverse_chamfer_back(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        fillet = Chamfer(r)
        self._add_back_edges(
            fillet, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def reverse_chamfer_front(
        self, r=2, *, left=False, right=False, top=False, bottom=False
    ):
        fillet = Chamfer(r)
        self._add_front_edges(
            fillet, left=left, right=right, top=top, bottom=bottom
        )
        return self

    def reverse_chamfer_bottom(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        fillet = Chamfer(r)
        self._add_bottom_edges(
            fillet, left=left, right=right, front=front, back=back
        )
        return self

    def reverse_chamfer_top(
        self, r=2, *, left=False, right=False, front=False, back=False
    ):
        fillet = Chamfer(r)
        self._add_top_edges(
            fillet, left=left, right=right, front=front, back=back
        )
        return self

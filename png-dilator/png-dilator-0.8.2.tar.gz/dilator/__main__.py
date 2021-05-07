'''
Author: GT<caogtaa@gmail.com>
Date: 2020-12-24 11:14:35
LastEditors: GT<caogtaa@gmail.com>
LastEditTime: 2021-05-07 14:09:46
'''
import os
import cv2
import numpy as np
import copy
import fire
from os import walk

class Dilator(object):
	'''
	Dilate texture with low alpha pixel to prevent "black edge" when rendered by GL\n
		dilator dilate_dir $your_dir
		dilator dilate $input_file_path $output_file_path
	'''

	def list_png_files(self, dir, output):
		root, sub_dirs, file_names = next(walk(dir))
		output.extend([os.path.join(root, x) for x in file_names if os.path.splitext(x)[1] == '.png'])
		for sub_dir in sub_dirs:
			self.list_png_files(os.path.join(root, sub_dir), output)

	def dilate_dir(self, dir):
		file_paths = []
		self.list_png_files(dir, file_paths)
		print('\n'.join(file_paths))

		for file_path in file_paths:
			self.dilate(file_path, file_path)

	def dilate(self, input_path, output_path):
		print("[DILATOR] Dilating %s" % input_path)

		# to support Unicode path, do not use cv2.imread directly
		origin_data = cv2.imdecode(
			np.fromfile(input_path, dtype=np.uint8),
			cv2.IMREAD_UNCHANGED)

		# origin_data = cv2.imread(input_path, -1)
		row, col, channel = origin_data.shape
		if channel == 3:
			# do not process if image has no alpha channel
			print("[DILATOR] Texture %s has no alpha channel, ignore" % input_path)
			return

		result = copy.deepcopy(origin_data)
		
		for i in range(0, row):
			for k in range(0, col):
				color = origin_data[i][k]
				if color[3] >= 3:
					# alpha already larger than threshold
					continue

				# pick colors from 8 directions, ignore colors whose alpha < 30
				# 这么做对同一张图重复扩边不会使扩边增长
				r = 0
				g = 0
				b = 0
				count = 0
				for x in range(-1, 2):
					i_x = i + x
					if i_x < 0 or i_x >= row:
						continue

					for y in range(-1, 2):
						if x == 0 and y == 0:
							# ignore center point
							continue

						k_y = k + y
						if k_y < 0 or k_y >= col:
							continue

						c2 = origin_data[i_x][k_y]
						if c2[3] < 30:
							continue

						# this color is considerable
						count += 1
						r += c2[0]
						g += c2[1]
						b += c2[2]
				# end 8 directions check

				if count > 0:
					# use average color from neighbors
					# alpha = 3
					out = result[i][k]
					out[0] = r / count
					out[1] = g / count
					out[2] = b / count
					out[3] = 3
		
		old_size = os.path.getsize(input_path)

		# to support Unicode path, do not use cv2.imwrite directly
		# cv2.imwrite(output_path, result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
		is_success, result_buf = cv2.imencode(".png", result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
		if is_success:
			result_buf.tofile(output_path)
			print("[DILATOR] Dilate '%s'->'%s' finished" % (input_path, output_path))

			new_size = os.path.getsize(output_path)
			print("[DILATOR] After dialtion file size %sK -> %sK" % (old_size / 1000, new_size / 1000))
		else:
			print("[DIALTOR] Encode image %s failed" % input_path)

	def for_8_dirs(self, img_data, pred, dir_cb):
		row, col, channel = img_data.shape
		for i in range(0, row):
			for k in range(0, col):
				color_c = img_data[i][k]
				if not pred(color_c):
					continue

				for x in range(-1, 2):
					i_x = i + x
					if i_x < 0 or i_x >= row:
						continue

					for y in range(-1, 2):
						if x == 0 and y == 0:
							# ignore center point
							continue

						k_y = k + y
						if k_y < 0 or k_y >= col:
							continue

						color_dir = img_data[i_x][k_y]
						dir_cb(color_c, color_dir)

	def sdf_bfs(self, img_data):
		row, col, channel = img_data.shape

		visited = np.zeros(shape=(row, col), dtype=np.uint8)
		qu = np.zeros(shape=(row * col, 2), dtype=np.uint16)		# qu[k] = (x, y)
		qlen = 0

		for i in range(0, row):
			for k in range(0, col):
				color_c = img_data[i][k]
				if color_c[2] > 0:
					# has red component, record it
					visited[i][k] = 1
					qu[qlen][0] = i
					qu[qlen][1] = k
					qlen += 1

		index = 0		# iterator
		while index < qlen:
			pos = qu[index]
			i = pos[0]
			k = pos[1]
			for x in range(-1, 2):
				i_x = i + x
				if i_x < 0 or i_x >= row:
					continue

				for y in range(-1, 2):
					if x == 0 and y == 0:
						# ignore center point
						continue

					k_y = k + y
					if k_y < 0 or k_y >= col:
						continue

					if img_data[i_x][k_y][3] <= 3:
						# transparent pixel, means not inside mask
						continue

					if visited[i_x][k_y] == 1:
						# already visited
						continue

					r_v = img_data[i][k][2]
					if r_v == 255:
						img_data[i_x][k_y][2] = 255
					else:
						img_data[i_x][k_y][2] = r_v + 1

					visited[i_x][k_y] = 1
					qu[qlen][0] = i_x
					qu[qlen][1] = k_y
					qlen += 1

			index += 1

	def sdf(self, input_path, output_path):
		print("[DILATOR] Calculate SDF %s" % input_path)

		# to support Unicode path, do not use cv2.imread directly
		origin_data = cv2.imdecode(
			np.fromfile(input_path, dtype=np.uint8),
			cv2.IMREAD_UNCHANGED)

		# origin_data = cv2.imread(input_path, -1)
		row, col, channel = origin_data.shape
		if channel == 3:
			# do not process if image has no alpha channel
			print("[DILATOR] Texture %s has no alpha channel, ignore" % input_path)
			return

		result = copy.deepcopy(origin_data)

		def dye_red_edge(c0, c1):
			if c1[3] > 3:
				c1[2] = 128					# 128为基础值

		# 对图像边缘染色
		self.for_8_dirs(result, lambda c: c[3] <= 3, dye_red_edge)
		self.sdf_bfs(result)

		is_success, result_buf = cv2.imencode(".png", result, [cv2.IMWRITE_PNG_COMPRESSION, 9])
		if is_success:
			result_buf.tofile(output_path)
		else:
			print("[DIALTOR] Calculate SDF %s failed" % input_path)

def main():
	fire.Fire(Dilator)

if __name__ == "__main__":
    main()

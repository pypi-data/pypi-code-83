
def minDist(atomList1, atomList2):
    dMin = 9999999.99999
    for v1 in [ numpy.array((a.x ,a.y, a.z)) for a in atomList1 ]:
        for v2 in [ numpy.array((b.x ,b.y, b.z)) for b in atomList2 ]:
            d = numpy.linalg.norm(v1 - v2)
            if d < dMin:
                dMin = d
    return dMin


def euclidianDist(atom1, atom2):
    mtx_atom1 = numpy.array(atom1.coordinates)
    mtx_atom2 = numpy.array(atom2.coordinates)
    return numpy.linalg.norm(mtx_atom1 - mtx_atom2)


class Cell(object):
    def __init__(self, iLabel, jLabel, value):
        self.iLabel = iLabel
        self.jLabel = jLabel
        self.value = value

    def __str__(self):
        return '(' + self.iLabel + ', ' + self.jLabel + ') : ' + str(self.value)



class MeshMap(object):
    def __init__(self, s1, s2):
        pass


class ContactMap(object):
    def __init__(self, s1, s2):
        self.nb_raws = s1.residueNumber
        self.nb_columns = s2.residueNumber
        self.mtx = numpy.zeros((self.nb_raws, self.nb_columns))

        self._resArrayOne = [ x for x in s1.byres() ]
        self._resArrayTwo = [ x for x in s2.byres() ]

        self.rl = [r.id for r in self._resArrayOne]
        self.cl = [r.id for r in self._resArrayTwo]

        for i1, r1 in enumerate(self._resArrayOne):
            for i2, r2 in enumerate(self._resArrayTwo):
                self.mtx[i1, i2] = minDist(r1, r2)

    # matrix element accessor along with row/column label, mostly for inspection
    def __getitem__(self, tup):
        x, y = tup
        return Cell(self.rl[x], self.cl[y], self.mtx[x, y])

    def __str__(self):
        asString = 'Contact map ' + str(len(self.rl)) + 'x' + str(len(self.cl)) + '\n'
        asString += '\t\t' + ''.join(["%9s" % r for r in self.cl]) + '\n'
        for i, row in enumerate(self.mtx):
            asString += "%9s" % self.rl[i]
            asString += ' '.join(["%9.1f" % d for d in row])
            asString += '\n'
        return asString

    def Q(self, d=4.5):
        f = lambda x: 1 if x < d else 0
        DistToQ = numpy.vectorize(f)
        return DistToQ(self.mtx)

    def residuesInterfacialBool(self, d=4.5):
        q = self.Q(d)
        def f(row):
            if numpy.sum(row) > 0:
                return 1
            return 0

        return interfaceBoolList( [({ 'num' : r.num, 'name' : r.name, 'chain' : r.chain }, f(q[i])) for i,r in enumerate(self._resArrayOne)],
            [({ 'num' : r.num, 'name' : r.name, 'chain' : r.chain}, f(q.T[i])) for i,r in enumerate(self._resArrayTwo)] )

    def weighted_contact_number(self):
        mtx = numpy.zeros((self.nb_raws, self.nb_columns))

        for i in range(len(self._resArrayOne)):
            for j in range(len(self._resArrayTwo)):
                if i != j:
                    mtx[i, j] = 1/(self.mtx[i, j]**2)

        return mtx.sum(axis=1,dtype=float)


class ContactMap_intra(object):
    def __init__(self, struc, cutoff=5.0):
        self.nb = struc.residueNumber
        self.mtx = numpy.zeros((self.nb,self.nb))

        self._resArray = [ x for x in struc.byres() ]

        self.l = [r.id for r in self._resArray]

        self.counter_infcutoff = 0

        for i in range(len(self._resArray)):
            for j in range(i+1,len(self._resArray)):
                self.mtx[i, j] = minDist(self._resArray[i], self._resArray[j])

                if self.mtx[i, j] < cutoff:
                    self.counter_infcutoff += 1

    # matrix element accessor along with row/column label, mostly for inspection
    def __getitem__(self, tup):
        x, y = tup
        return Cell(self.l[x], self.l[y], self.mtx[x, y])

    def __str__(self):
        asString = 'Contact map intra ' + str(len(self.l)) + 'x' + str(len(self.l)) + '\n'
        asString += '\t\t' + ''.join(["%9s" % r for r in self.l]) + '\n'
        for i, row in enumerate(self.mtx):
            asString += "%9s" % self.l[i]
            asString += ' '.join(["%9.1f" % d for d in row])
            asString += '\n'
        return asString

    def weighted_contact_number(self):
        mtx = numpy.zeros((self.nb,self.nb))

        for i in range(len(self._resArray)):
            for j in range(i+1,len(self._resArray)):
                mtx[i, j] = 1/(self.mtx[i, j]**2)

        symetric_mtx = mtx + mtx.T

        return symetric_mtx.sum(axis=1,dtype=float)


class ContactMap_intra_grid(object):
    def __init__(self, struc, cutoff=5.0):
        self.struc = struc
        self._resArray = self.struc.getResID
        self._residuePairRegistry = {}
        self.cutoff = cutoff
        self._parsing()
        self._build_grid()
        self._list_next_unique_neighbors()
        self._calculate_distances()
        self._build_ContactMap()

    # matrix element accessor along with row/column label, mostly for inspection
    def __getitem__(self, tup):
        x, y = tup
        return Cell(self._resArray[x], self._resArray[y], self.mtx[x, y])

    def __str__(self):
        asString = 'Contact map intra grid ' + str(len(self._resArray)) + 'x' + str(len(self._resArray)) + '\n'
        asString += '\t\t' + ''.join(["%9s" % r for r in self._resArray]) + '\n'
        for i, row in enumerate(self.mtx):
            asString += "%9s" % self._resArray[i]
            asString += ' '.join(["%9.1f" % d for d in row])
            asString += '\n'
        return asString

    def _parsing(self):
        # ---
        # PARSING
        # ---

        self.counter_atoms = 0

        self.min_x,self.min_y,self.min_z = 9999999.99999,9999999.99999,9999999.99999
        self.max_x,self.max_y,self.max_z = -9999999.99999,-9999999.99999,-9999999.99999

        for atom in self.struc.atomRecord:
            # ---
            # GET MINIMUMS AND MAXIMUMS OF EACH COORDINATES X,Y,Z
            # ---

            self.counter_atoms += 1

            self.min_x = atom.x if atom.x < self.min_x else self.min_x
            self.min_y = atom.y if atom.y < self.min_y else self.min_y
            self.min_z = atom.z if atom.z < self.min_z else self.min_z

            self.max_x = atom.x if atom.x > self.max_x else self.max_x
            self.max_y = atom.y if atom.y > self.max_y else self.max_y
            self.max_z = atom.z if atom.z > self.max_z else self.max_z

        # ---
        # GET DIMENSIONS OF THE 3D GRID
        # ---

        self.dim_x = int(math.floor((self.max_x-self.min_x)/self.cutoff))+1
        self.dim_y = int(math.floor((self.max_y-self.min_y)/self.cutoff))+1
        self.dim_z = int(math.floor((self.max_z-self.min_z)/self.cutoff))+1

    def _coor_Cartesian2Grid(self,atom):
        # ---
        # GET AN ATOM AND RETURN ITS NORMALIZED COORDINATES
        # ---
        return [int(math.floor((atom.x-self.min_x)/self.cutoff)),int(math.floor((atom.y-self.min_y)/self.cutoff)),int(math.floor((atom.z-self.min_z)/self.cutoff))]

    def _build_grid(self):
        self.grid_3D = numpy.empty((self.dim_x,self.dim_y,self.dim_z),dtype=numpy.object_)
        self.grid_3D.fill([])
        self.grid_3D = numpy.frompyfunc(list,1,1)(self.grid_3D)

        for atom in self.struc.atomRecord:
            [i,j,k] = self._coor_Cartesian2Grid(atom)
            self.grid_3D[i,j,k].append(atom)

    def _iter_next_unique_neighbors(self, x, y, z):
        value_list = []

        for i in range(x, x+2):
            if i == self.dim_x:
                break

            for j in range(y-1, y+2):
                if j < 0:
                    continue
                if j == self.dim_y:
                    break

                for k in range(z-1, z+2):
                    if k < 0:
                        continue
                    if k == self.dim_z:
                        break

                    if ( i > x or j > y or (j > y-1 and k > z-1) ) and self.grid_3D[i,j,k] != []:
                        value_list.append(self.grid_3D[i,j,k])

        return value_list

    def _list_next_unique_neighbors(self):
        self.value_LIST = []

        for i in range(self.dim_x):
            for j in range(self.dim_y):
                for k in range(self.dim_z):

                    if self.grid_3D[i,j,k] != []:
                        self.value_LIST.append(self._iter_next_unique_neighbors(i,j,k))

    def _calculate_distances(self):
        self.dist_LIST = []
        self.counter_dist = 0

        for i in range(len(self.value_LIST)):
            current = self.value_LIST[i][0]
            neighbors_flat_LIST = [j for i2 in self.value_LIST[i][1:] for j in i2]

            for j in range(len(current)):

                for k in range(j+1,len(current)):
                    self.dist_LIST.append([[current[j],current[k]],euclidianDist(current[j],current[k])])
                    self.counter_dist += 1

                for l in range(len(neighbors_flat_LIST)):
                    self.dist_LIST.append([[current[j],neighbors_flat_LIST[l]],euclidianDist(current[j],neighbors_flat_LIST[l])])
                    self.counter_dist += 1

    def _build_ContactMap(self):
        self.mtx = numpy.empty((len(self._resArray),len(self._resArray)),dtype=float)
        self.mtx.fill(9999999.99999)

        for idx in self.dist_LIST:
            i = self._resArray.index(idx[0][0].getResID)
            j = self._resArray.index(idx[0][1].getResID)
            if idx[1] > self.cutoff:
                continue
            if idx[1] < self.mtx[i, j] and i != j:
                self.mtx[i, j] = idx[1]
                self.mtx[j, i] = idx[1]
                self._registerResiduePair(i, j)

    def _registerResiduePair(self, i, j):
        (resID_A, resID_B) = (self._resArray[i], self._resArray[j]) if i < j else (self._resArray[j], self._resArray[i])
        if resID_A not in self._residuePairRegistry:
            self._residuePairRegistry[resID_A] = [resID_B]
        elif resID_B not in self._residuePairRegistry[resID_A]:
            self._residuePairRegistry[resID_A].append(resID_B)


class ContactOrder(object):
    def __init__(self, struc_name, struc, cutoff=5.0):
        self._contiguous = None
        self.list_CO = []

        for curr_ch in struc.chainList:

            self.sub_struct = struc.chain(curr_ch)
            cm_intra = ContactMap_intra_grid(self.sub_struct,cutoff)
            counter,SUM = 0,0

            for i in range(len(cm_intra._resArray)):
                for j in range(i+1,len(cm_intra._resArray)):
                    if cm_intra.mtx[i, j] < cutoff:
                        SUM += abs(i-j)
                        counter += 1

            self.list_CO.append([struc_name,curr_ch,'{:.2f}'.format(float(SUM)/counter),self.contiguous])

    def __iter__(self):
        for item in self.list_CO:
            yield item

    @property
    def contiguous(self):
        if not self._contiguous:
            self._contiguous = True
            trace_list = [atom for atom in self.sub_struct.trace]
            for i in range(1,len(trace_list)):
                curr_atom = trace_list[i]
                prev_atom = trace_list[i-1]
                dist = minDist([curr_atom],[prev_atom])
                if float(dist) > 4.0:
                    self._contiguous = False
                    break
        return self._contiguous


class interfaceBoolList(object):
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def __getitem__(self, k):
        if(k == 0):
            l = self.l1
        elif(k == 1):
            l = self.l2
        else :
            raise ValueError("index \"" + str(k) + "\"out of bounds ")
        s = self.asString(l)
        return s

    def toList(self, k):
        data = []

        if(k == 0):
            l = self.l1
        elif(k == 1):
            l = self.l2
        else :
            raise ValueError("index \"" + str(k) + "\"out of bounds ")
        for d in l:
            data.append({ 'res' : d[0], 'cc' : d[1] })
        return data

    def asString(self, l):
        return '\n'.join([ "%4s %s %s %d" % (d[0]['num'], d[0]['name'], d[0]['chain'], d[1]) for d in l ])

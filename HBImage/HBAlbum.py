import threading
from multiprocessing.dummy import Pool as ThreadPool

from typing import List

from .HBImage import HBImage, HBCommon


class HBAlbum:
    
    def __init__(self,source = None,*args,**kwargs):
        self._album:List[HBImage] = []
        self._bookmark:int = 0

        if source:
            self.load(source)


    def __add__(self, other):
        if isinstance(other,HBAlbum):
            self.merge(other)
        elif isinstance(other,HBImage):
            self.append(other)
        else:
            raise AttributeError(f"{type(other)} cannot be added to the HBAlbum.")
        
        
    def __len__(self):
        return len(self._album)
    
    def __getitem__(self, key):
        return self._album[key]
    
    def __setitem__(self, key, value):
        if not isinstance(value,HBImage):
            raise AttributeError(f"{type(value)} cannot be added to the HBAlbum.")
        self._album[key] = value

    def __iter__(self):
        return iter(self._album)

    @property
    def is_empty(self):
        return len(self._album) == 0
    
    @property
    def length(self):
        return len(self._album)

    @property
    def marked_image(self):
        if self.is_empty:
            return None
        return self._album[self._bookmark]
    
    @property
    def bookmark(self):
        return self._bookmark

    @bookmark.setter
    def bookmark(self, index:int):
        if index<=0 or self.is_empty:
            self._bookmark = 0
        elif index>=self.length:
            self._bookmark = self.length-1
        else:
            self._bookmark = index

    
    def append(self, hb_image:HBImage):
        if hb_image.is_empty:
            raise AttributeError(f"Append Nothing!")
        self._album.append(hb_image)
        
    def merge(self, hb_album:'HBAlbum'):
        self._album.extend(hb_album)
    
    def delete(self, index):
        if self.bookmark==(self.length-1):
            self.bookmark = self.length - 2
        self._album[index].image.close()
        del self._album[index]

            

    def insert(self, index, hbimage):
        self._album.insert(index, hbimage)
        if index>=self.bookmark:
            self.bookmark += 1

    def save(self, folder_path:str, filename_prefix=None, format:str=None):
        HBCommon.create_folder(folder_path)

        save_threads = []
        
        for image in self._album:
            img_name = image.information.get("filename")
            if filename_prefix:
                img_name += filename_prefix+'_'
            img_filepath = f"{folder_path}/{img_name}"
            
            save_threads.append(
                threading.Thread(
                    target=image.save, 
                    args=(img_filepath,format)
            ))
            
        for t in save_threads:
            t.start()
        for t in save_threads:
            t.join()
            
    def _save_single_image(self, folder_path:str, filename_prefix=None, format:str=None):
        pass



    def load_from_filepaths_no_thread(self, filepaths_list:List[str]):
        if not filepaths_list:
            return False
        for filepath in filepaths_list:
            self.append(HBImage(filepath))

    
    def load(self, source):
        """"""
        if isinstance(source, list):
            if isinstance(source[0], str):
                self.load_from_filepaths(source)
            elif isinstance(source[0], HBImage):
                self._album = source
            else:
                raise AttributeError(f"{type(source)} cannot be added to the HBAlbum.")
        
        elif isinstance(source, str):
            """
            If source is a txt file, assume it contain the images' url.
            Read file into list[urls], then use these urls call function:"load_from_filepaths".
            """
            if HBCommon.get_file_format(source)=="txt":
                self.load_from_filepaths(HBCommon.load_file_txt(source))

    

    def load_from_filepaths(self, filepaths_list:List[str]):
        if not filepaths_list:
            return None
        self._load_fail = []
        #self._album = [None]*len(filepaths_list)

        with ThreadPool() as p:
            self._album = p.map(self._get_load_from_filepath, filepaths_list)



    def _get_load_from_filepath(self, filepath:str):
        if not filepath:
            return None

        try:
            return HBImage(filepath)
        except FileNotFoundError as err:
            print(err)
            self._load_fail.append([filepath, err])
            return None



## Kyle Fitch
## FTP script for ARM data (on my iMac at UU), specifically for Spyder (Python
# 2.7) which requires a different directory naming convention; downloads .tar 
# files using ftp connection with ARM archive; then unpacks
# the .tar files (one .tar can be thousands of .png and .txt files); then gives
# them a shorter filename and sorts them based on the new filename, which contains
# metadata about the date and time
## 5 Oct 17
# test
# set ARM order number
num = 'fitchk1/215357'
#num = 'kushalievd1/212080'

# ARM archive FTP site
archive = 'ftp.archive.arm.gov'

# directories to download to
#data_folder = '/Volumes/garrett-home/u1147787/mascpy/Data'
data_folder = '/uufs/chpc.utah.edu/common/home/garrett-group3/fitch/Data'
downloads = data_folder + '/downloads'
extracted = downloads + '/extracted'
mwr = data_folder + '/ARM/MWR-LWP' 
mwrret2turn = data_folder + '/ARM/LWP_corr_Maahn'
met = data_folder + '/ARM/MET/OLI'
dlprof = data_folder + '/ARM/dlprof'
ecor = data_folder + '/ARM/ECOR'
cld_thick = data_folder + '/ARM/Cloud_Thickness'
radar = data_folder + '/ARM/Radar'
skyrad = data_folder + '/ARM/SKYRAD-Tcb'
new_cld_thick = data_folder + '/ARM/New_Cloud_Thickness'
ceil = data_folder + '/ARM/CEIL'
kollias = data_folder + '/ARM/Kollias'
pmicro = data_folder + '/ARM/pmicro'
sonde = data_folder + '/ARM/sonde'
mpl = data_folder + '/ARM/MPL'
barrow = met + '/Barrow' + '/2008'
data = pmicro + '/data'
crsim = data + '/crsim/ARM_Summer2018_nc4'
csapr = data + '/csapr'
nexrad = data + '/nexrad'
windretrieval = data + '/windretrieval'
wrf = data + '/wrf'
csapr_cart = data + '/csapr/mmcg/sgp.I7/20110520/20110520-hr09'
epic_cloud = data_folder + '/EPIC/EPIC_L2_CLOUD'
epic_geoloc = data_folder + '/EPIC/EPIC_L1A'
dani = data_folder + '/ARM/Daniyar'
#file_type = '.cdf'
file_type = '.nc'
#file_type = '.tar'

mydir = dlprof

# set email
email = 'kyle.fitch@utah.edu'
#email = 'daniyarkushaliev@gmail.com'

# import 
import ftplib

# import sys for 'getFile' function
#import sys

# define the 'getFile' function
def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print "Error"
        
# change directory
import os
os.chdir(mydir)

# start ftp
ftp = ftplib.FTP(archive)
ftp.login('ftp',email)

# change to directory for specific ARM data order
ftp.cwd(num+'/')

# store ftp text info into list of strings
data = []
ftp.dir(data.append)
# only want .tar files
data = [ x for x in data if file_type in x ]
size = len(data)
print '# of files to download: ',size

# download file loop
for x in range(0,size):
	d_string = data[x]
	d_file = d_string.split()[-1]
	getFile(ftp,d_file)
	print 'Downloaded ' + d_file

# end ftp
ftp.quit()

#dir_list = os.listdir(downloads)
#dir_list = [ x for x in dir_list if ".tar" in x ]
#dir_list.sort()
#dir_size = len(dir_list)

#for m in range(0,dir_size):
	
#    fn = str(dir_list[m])
#    tar = tarfile.open(fn)
#    tar.extractall(path = extracted)
#    tar.close()
	
#    print 'Unpacked ' + fn

# lastly, delete all the .tar files in the downloads folder
#for y in range(0,dir_size):
#	os.remove(dir_list[y])
    
# now go to 'extracted' folder to rename and sort all files
#os.chdir(extracted)

#file_list = os.listdir(extracted)
#file_list = [ x for x in file_list if "oli" in x ]
#file_list.sort()
#file_list_size = len(file_list)

#for n in range(0,file_list_size):
 #   fn = str(file_list[n])
  #  new_fn = fn[33:]
   # current_path = extracted + '/' + fn
    #new_name_path = extracted + '/' + new_fn
    #os.rename(current_path,new_name_path)
    #yr = new_fn[13:17]
    #mm = new_fn[17:19]
    #dd = new_fn[19:21]
    #hr = new_fn[22:24]
	
    # move file to proper folder
    #new_path = data_folder + '/' + yr + '/' + yr + '_' + mm + '/' + yr + '_' + mm + '_' + dd + '/' + 'masc_' + yr + '.' + mm + '.' + dd + '_Hr_' + hr + '/' + new_fn

    # even though this uses 'rename', it is actually moving the file
    #os.rename(new_name_path, new_path)
    #print new_fn, ' moved to: ', new_path

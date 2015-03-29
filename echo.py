
class echo():                                                                      
	HEADER = '\033[95m'                                                        
	OKBLUE = '\033[94m'                                                        
	OKGREEN = '\033[92m'                                                       
	WARNING = '\033[93m'                                                       
	FAIL = '\033[91m'                                                          
	ENDC = '\033[0m'                                                           
	@staticmethod                                                              
	def normal(info):                                                      
	        return echo.OKBLUE + str(info) + echo.ENDC                           
                                                                           
	@staticmethod                                                              
	def high(info):                                                        
	        return echo.OKGREEN + str(info) + echo.ENDC                          
	                                                                           
	@staticmethod                                                              
	def fail(info):                                                        
	        return echo.FAIL + str(info) + echo.ENDC    
	@staticmethod
	def no(info):
		return info       
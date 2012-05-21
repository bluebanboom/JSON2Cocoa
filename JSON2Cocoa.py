# encoding:utf8
import os
import codces

TypeEncodeMethods = {'NSInteger':['numberWithInt','intValue'],
        'BOOL':['numberWhitBool', 'boolValue'],}

class CocoaProperty:
    def __init__(self):
        self.name = ''
        self.valType = ''
        self.jsonKey = ''
        self.isObject = True

class CreateCode:
    def __init__(self):
        self.interfaceName = ''
        self.propertys = []

    def CreateHeader(self):
        codes = '#import <Foundation/Foundation.h>\n'
        codes += '@interface %s : NSObject <NSCoding>\n' % self.interfaceName

        for oneProperty in self.propertys:
            if oneProperty.isObject:
                codes += '@property (nonatomic, strong) %s *%s\n' % (oneProperty.valType, oneProperty.name)
            else:
                codes += '@property (nonatomic, assign) %s %s\n' % (oneProperty.valType, oneProperty.name)
        
        codes += '- (id)initWithDict:(NSDictionary *)dict;\n\n@end'

        outfile = codces.open('%s.h' % self.interfaceName, 'w', 'utf8')
        outfile.write(codes)
        outfile.close()

    def CreateM(self):
        pass

    def CreateDealloc(self):
        pass

    def CreateInit(self):
        pass

    def CreateEncode(self):
        pass

    def CreateDecode(self):
        pass

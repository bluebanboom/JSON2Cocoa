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
        codes = '- (void)dealloc\n{\n'
        for oneProperty in self.propertys:
            if oneProperty.isObject:
                codes += '\t[%s release];\n' % (oneProperty.valType, oneProperty.name)

        codes += '\t[super dealloc];\n}\n'
        return codes

    def CreateInit(self):
        codes = '- (id)initWithDict:(NSDictionary *)dict\n{\n\tself = [super init];\n'
        codes += '\tif (self) {\n'
        for oneProperty in self.propertys:
            if oneProperty.isObject:
                codes += '\t\tself.%s = [dict objectForKey:%s];\n' % (oneProperty.name, oneProperty.jsonKey)
            else:
                codes += '@property (nonatomic, assign) %s %s\n' % (oneProperty.valType, oneProperty.name)
        codes += '\t}\n\treturn self;\n}'

    def CreateEncode(self):
        pass

    def CreateDecode(self):
        pass

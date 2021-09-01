import unittest
import methods

class TestMethods(unittest.TestCase):
    def test_getKillerName(self):
        result = methods.getKillerName('23:06 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, '<world>')
        result = methods.getKillerName('23:06 Kill: 1022 2 22: Isgalamido killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKillerName('23:06 Kiddddddll: 10asdasdasd: Isgalamido killed Isgalamasdasdido basdasdasdy MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKillerName(' :  : : Dono da Bola killed Isgalamasdasdido basdasdasdy MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Dono da Bola')
        result = methods.getKillerName(' :  : : Isgalamido')
        self.assertEqual(result, 'Isgalamido')
    
    def test_getKilledName(self):
        result = methods.getKilledName('23:06 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName('23:06 Kill: 1022 2 22: Isgalamido killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName(' :  : : Isgalamido killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName(' :  : : <world> killed Isgalamido by')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName(' :  : : <world> killed Isgalamido by sda')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName(' :  : : <world> killed Isgalamido by ')
        self.assertEqual(result, 'Isgalamido')
        result = methods.getKilledName('23:06 Kiddddddll: 10asdasdasd: Isgalamido killed Isgalamasdasdido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'Isgalamasdasdido')
    
    def test_getCauseOfDeath(self):
        result = methods.getCauseOfDeath('23:06 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'MOD_TRIGGER_HURT')
        result = methods.getCauseOfDeath('23:06 Kill: 1022 2 22: Isgalamido killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'MOD_TRIGGER_HURT')
        result = methods.getCauseOfDeath(' :  : : Isgalamido killed Isgalamido by MOD_TRIGGER_HURT')
        self.assertEqual(result, 'MOD_TRIGGER_HURT')
        result = methods.getCauseOfDeath(' :  : : <world> killed Isgalamido by')
        self.assertEqual(result, '')
        result = methods.getCauseOfDeath(' :  : : <world> killed Isgalamido by sda')
        self.assertEqual(result, 'sda')
        result = methods.getCauseOfDeath(' :  : : <world> killed Isgalamido by ')
        self.assertEqual(result, '')

    def test_getPlayerName(self):
        result = methods.getPlayerName('21:51 ClientUserinfoChanged: 3 n\Dono da Bola\\t\\0\model\sarge/krusade\hmodel\sarge/krusade\g_redteam\\g_blueteam\\c1\5\c2\5\hc\95\w\0\l\0\tt\0\tl\0')
        self.assertEqual(result, 'Dono da Bola')
        result = methods.getPlayerName('21:53 ClientUserinfoChanged: 3 n\Mocinha\\t\0\model\sarge\hmodel\sarge\g_redteam\\g_blueteam\\c1\4\c2\5\hc\95\w\0\l\0\tt\0\tl\0')
        self.assertEqual(result, 'Mocinha')
        result = methods.getPlayerName('21231231: 3 n\Mocinha\\t\\0\modd4234444444342m\\g_blueteam\\c1\4\c2\5\hc\95\w\0\l\0\tt\0\tl\0')
        self.assertEqual(result, 'Mocinha')
        result = methods.getPlayerName('21231231: 3 n\sda\\t\\0\modd4234444444342m\\g_blueteam\\c1\4\c2\5\hc\95\w\0\l\0\tt\0\tl\0')
        self.assertEqual(result, 'sda')
        
        
        
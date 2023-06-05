from OriginExt import OriginExt
import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

x_data = df['reaction coordinate'].tolist()
y_data = df['gibbs energy'].tolist()

op = OriginExt()
op.new_sheet()
op.put_datasheet('x', x_data)
op.put_datasheet('y', y_data)
op.exec_command('layer.x.label$ = "Reaction Coordinate"')
op.exec_command('layer.y.label$ = "Gibbs Energy (kJ/mol)"')
op.exec_command('layer.y.type = 5')
op.exec_command('layer.y.comment$ = "Curve1"')
op.exec_command('layer.y.color = 3')
op.exec_command('page.width = 8')
op.exec_command('page.height = 6')
op.export('graph', 'jpg', 'graph.jpg')

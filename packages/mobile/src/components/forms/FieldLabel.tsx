import React from 'react';
import {StyleSheet, Text} from 'react-native';
import {colors, spacing, typography} from '../../theme';

export const FieldLabel = ({children}: {children: React.ReactNode}) => (
  <Text style={styles.label}>{children}</Text>
);

const styles = StyleSheet.create({
  label: {
    color: colors.text,
    fontSize: typography.caption,
    fontWeight: '800',
    marginBottom: spacing.xs,
    marginTop: spacing.md,
    textTransform: 'uppercase',
  },
});
